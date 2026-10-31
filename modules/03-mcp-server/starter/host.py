"""
A minimal MCP *host*: it connects a real LLM to your MCP server and runs the
full agent loop, so you watch a model decide to call your tools -- using a
FREE model, no Claude subscription required.

It talks to any OpenAI-compatible endpoint. Two free ways to run it:

  A) OLLAMA (fully local, no API key, no signup) -- recommended
     1. Install Ollama from https://ollama.com and start it.
     2. Pull a tool-capable model, e.g.:  ollama pull qwen2.5
     3. (defaults already point here -- just run it)
        python host.py "add 128 and 457"

  B) GROQ (free cloud API key, very fast)
     1. Get a free key at https://console.groq.com/keys
     2. Set env vars, then run:
        # Git Bash / macOS / Linux:
        export LLM_BASE_URL=https://api.groq.com/openai/v1
        export LLM_API_KEY=gsk_your_key_here
        export LLM_MODEL=llama-3.3-70b-versatile
        python host.py "how many words are in: the quick brown fox"

Any OpenAI-compatible endpoint works the same way (OpenRouter, LM Studio, etc.) --
set LLM_BASE_URL / LLM_API_KEY / LLM_MODEL and go.

Needs:  pip install -r requirements.txt   (installs the `openai` client too)
Built against MCP Python SDK 2.x. The spec moves fast -- if an import fails,
check https://modelcontextprotocol.io/docs/develop/build-server .
"""
import json
import os
import sys

import anyio
from mcp import Client, StdioServerParameters
from mcp.types import TextContent
from openai import OpenAI

# --- model config: defaults to local Ollama, override with env vars for Groq etc.
BASE_URL = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1")
API_KEY = os.environ.get("LLM_API_KEY", "ollama")   # Ollama ignores the key
MODEL = os.environ.get("LLM_MODEL", "qwen2.5")

# Launch server.py with the same Python running this host.
server = StdioServerParameters(command=sys.executable, args=["server.py"])


def to_openai_tools(mcp_tools):
    """Turn MCP tool definitions into the OpenAI function-calling schema."""
    return [
        {
            "type": "function",
            "function": {
                "name": t.name,
                "description": t.description or "",
                "parameters": t.input_schema,
            },
        }
        for t in mcp_tools
    ]


def text_of(result):
    """Flatten an MCP tool result's content blocks into a string."""
    parts = [b.text for b in result.content if isinstance(b, TextContent)]
    return "\n".join(parts) if parts else str(result.structured_content)


def text_json_toolcall(content, tool_names):
    """Fallback for small local models that emit a tool call as plain JSON text
    (e.g. {"name": "add", "arguments": {...}}) instead of a native tool_calls
    field. Returns (name, args) if the content looks like one of our tools."""
    if not content:
        return None
    try:
        data = json.loads(content.strip())
    except (ValueError, TypeError):
        return None
    if (isinstance(data, dict) and data.get("name") in tool_names
            and isinstance(data.get("arguments"), dict)):
        return data["name"], data["arguments"]
    return None


async def main() -> None:
    prompt = " ".join(sys.argv[1:]) or "Add 128 and 457 using your tools."
    llm = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    async with Client(server) as mcp:
        tools = to_openai_tools((await mcp.list_tools()).tools)
        tool_names = {t["function"]["name"] for t in tools}
        print(f"[host] model={MODEL}  tools={sorted(tool_names)}\n")

        messages = [{"role": "user", "content": prompt}]

        # The agent loop: ask the model; if it wants a tool, call it on the MCP
        # server and feed the result back; repeat until it answers in words.
        for _ in range(6):  # safety cap on rounds
            resp = llm.chat.completions.create(
                model=MODEL, messages=messages, tools=tools, temperature=0,
            )
            msg = resp.choices[0].message

            # Path 1 (the standard one Groq and strong models use): native
            # tool_calls. Each result goes back as a dedicated "tool" message.
            if msg.tool_calls:
                messages.append(msg)
                for call in msg.tool_calls:
                    args = json.loads(call.function.arguments or "{}")
                    print(f"[model wants] {call.function.name}({args})")
                    output = text_of(await mcp.call_tool(call.function.name, args))
                    print(f"[tool result] {output}")
                    messages.append({"role": "tool",
                                     "tool_call_id": call.id, "content": output})
                continue

            # Path 2 (fallback): the model wrote the tool call as JSON text.
            fallback = text_json_toolcall(msg.content, tool_names)
            if fallback:
                name, args = fallback
                print(f"[model wants] {name}({args})   (emitted as text)")
                output = text_of(await mcp.call_tool(name, args))
                print(f"[tool result] {output}")
                messages.append({"role": "assistant", "content": msg.content})
                messages.append({"role": "user",
                                 "content": f"The {name} tool returned {output}. "
                                            "Answer the original question in one sentence."})
                continue

            # No tool wanted -> this is the final answer.
            print(f"\n[model] {msg.content}")
            return

        print("[host] stopped after too many tool rounds")


if __name__ == "__main__":
    anyio.run(main)
