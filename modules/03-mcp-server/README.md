# 03: Set up your own MCP server

**You'll build:** a small MCP server that exposes a few tools, tested with a local client and then connected to Claude Desktop so a model can call them
**You'll understand:** how LLMs reach external tools — the backbone of every agentic system — and what a "tool" actually is on the wire
**Time:** one in-person workshop (about 2 hours)
**Format:** in person, bring a laptop

> **This spec moves fast.** MCP changes often. This module was built on **2026-10-31** against the **Python SDK 2.x** (`mcp 2.x`) and protocol version **2026-07-28**. If an import or command below fails, the API moved — check the current [build-a-server guide](https://modelcontextprotocol.io/docs/develop/build-server) and [`mcp` on PyPI](https://pypi.org/project/mcp/), and update your code to match. Facilitators: re-verify this module against the live docs before each cohort.

You work in [`starter/`](starter/), which ships a working one-tool server and a test client, so you see a tool get called **on day one** — no LLM or API key needed. The payoff checkpoint connects it to a real model.

## The mental model (read once)

An LLM can only produce text. It can't read a file, hit an API, or do math reliably — unless you give it **tools**. MCP (**Model Context Protocol**) is the standard way to do that:

- Your **server** exposes functions (tools), each with a name, a description, and a typed schema for its arguments.
- A **client** (the test client here, the `host.py` free-model host, the MCP Inspector, or Claude Desktop) connects, asks the server to **list** its tools, and can **call** them.
- When a model is wired to the client, *the model* decides which tool to call and with what arguments, based on each tool's name and description. The server runs the function and hands back the result.

So the loop is: **model reads tool descriptions → picks one → client calls it on the server → result goes back to the model.** You're building the server half.

The default transport is **stdio**: the client launches your server as a subprocess and they speak JSON-RPC over stdin/stdout. (For remote servers the current transport is **Streamable HTTP** — see Going further.)

## Prerequisites

Before the workshop:

- **Python 3.10+** — `python --version`.
- A virtual environment with the SDK installed:
  ```bash
  cd modules/03-mcp-server/starter
  python -m venv .venv
  # Windows (Git Bash):   source .venv/Scripts/activate
  # Windows (PowerShell):  .venv\Scripts\Activate.ps1
  # macOS / Linux:         source .venv/bin/activate
  pip install -r requirements.txt
  ```
- **For checkpoint 5 (watch a real model call your tools)** — pick one free option, no paid subscription needed:
  - **Ollama (local, free, no API key)** — install from [ollama.com](https://ollama.com), then pull a tool-capable model: `ollama pull qwen2.5`. This is the recommended path.
  - **Groq (free cloud API key, very fast)** — get a free key at [console.groq.com/keys](https://console.groq.com/keys).
  - **Claude Desktop (optional extra)** — if you already have [Claude Desktop](https://claude.ai/download), checkpoint 5 shows how to wire your server into it too.
- A code editor.

## Setup

With the venv active:

```bash
python client.py
```

You're set up when it prints:

```
Server exposes 1 tool(s):
  - add: Add two numbers and return the sum.
```

The client just launched your server as a subprocess, asked it for its tools, and listed them. That's the MCP handshake.

## Checkpoint 1: Run the server and call a tool

**Goal:** see a tool get called over MCP, end to end.

```bash
python client.py add a=2 b=3
```

**Check it:** the output includes

```
  text: 5
  structured: {'result': 5}
```

Two forms of the same answer: `text` is what's shown to the model, `structured` is the machine-readable return value your code would use. Open [`starter/server.py`](starter/server.py) and read the `add` function — the `@mcp.tool()` decorator and the type hints are the whole magic.

## Checkpoint 2: Add your own tool

**Goal:** expose a new tool with typed arguments and a good description.

In `server.py`, below `add`, add a tool (there's a commented example showing exactly this):

```python
@mcp.tool()
def word_count(text: str) -> int:
    """Count the words in a piece of text."""
    return len(text.split())
```

The SDK turns your **type hints** (`text: str`) into the argument schema and your **docstring** into the description the model reads. A clear docstring is not optional — it's how the model knows when to call your tool.

**Check it:**

```bash
python client.py                                   # word_count now in the list
python client.py word_count text="hello there world"
```

The call prints `text: 3` and `structured: {'result': 3}`.

## Checkpoint 3: Handle bad input with ToolError

**Goal:** fail safely, the way the protocol expects.

Add a tool that can reject its input:

```python
from mcp.server.mcpserver.exceptions import ToolError   # put with the imports at the top

@mcp.tool()
def sqrt(x: float) -> float:
    """Square root of a non-negative number."""
    if x < 0:
        raise ToolError("x must be non-negative")
    return x ** 0.5
```

The key idea: a tool that raises `ToolError` does **not** crash the client with an exception. It comes back as a normal **result** with `is_error` set — so the model can read the error message and try something else. That's why the test client checks `result.is_error` instead of wrapping the call in `try/except`.

**Check it:**

```bash
python client.py sqrt x=-9
```

prints `tool reported an ERROR:` and `text: Error executing tool sqrt: x must be non-negative`.

## Checkpoint 4: A tool that reaches outside

**Goal:** the actual point of MCP — give the model a capability it otherwise doesn't have.

Add a tool that reads a file from disk:

```python
@mcp.tool()
def read_file(path: str) -> str:
    """Return the text contents of a file on disk."""
    with open(path, encoding="utf-8") as f:
        return f.read()
```

A plain LLM can't read your files. With this tool it can — through you, on your machine, with whatever limits you put in the function. (Notice you'd want to validate `path` before shipping this for real; that gatekeeping is *your* job, and it's why running arbitrary servers is a trust decision.)

**Check it:**

```bash
echo "hello there world" > sample.txt
python client.py read_file path=sample.txt
```

returns the file's contents in `text:` and `structured:`.

## Checkpoint 5: Watch a real model call it

**Goal:** connect a real LLM to your server and watch *the model* decide to call your tool — using a **free** model.

This folder ships [`host.py`](starter/host.py): a minimal MCP **host** that runs the full agent loop — it lists your tools, hands them to a model, and when the model asks for one, calls it on your server and feeds the result back. It talks to any OpenAI-compatible endpoint, so the same script works with local Ollama or Groq's free API.

### Option A — Ollama (local, free, no API key) — recommended

1. Make sure Ollama is running and you've pulled a tool-capable model:
   ```bash
   ollama pull qwen2.5        # or: llama3.1  (both support tool calling)
   ```
2. `host.py` already defaults to Ollama. If you pulled a different model, set its name:
   ```bash
   # Git Bash / macOS / Linux:
   export LLM_MODEL=qwen2.5
   # PowerShell:  $env:LLM_MODEL = "qwen2.5"
   ```
3. Run it:
   ```bash
   python host.py "Use your tools to add 128 and 457, then tell me the answer."
   ```

### Option B — Groq (free cloud API key, very fast)

```bash
# Git Bash / macOS / Linux (PowerShell: use $env:NAME = "...")
export LLM_BASE_URL=https://api.groq.com/openai/v1
export LLM_API_KEY=gsk_your_free_key_here
export LLM_MODEL=llama-3.3-70b-versatile
python host.py "How many words are in: the quick brown fox jumps"
```

(Any OpenAI-compatible endpoint works — OpenRouter, LM Studio, etc. — by setting those three `LLM_*` variables.)

**Check it:** the output shows the model asking for your tool, the tool's result, and a final sentence that uses it:

```
[model wants] add({'a': 128, 'b': 457})
[tool result] 585

[model] The sum of 128 and 457 is 585.
```

You've closed the loop — a model reached your code. 🎉

> **Tool calls as text?** Some smaller local models emit a tool call as plain JSON text instead of the proper `tool_calls` field. `host.py` handles both: it uses the native field when present (what Groq and larger models do) and falls back to parsing the JSON otherwise, so it works across free models. If a model never calls the tool, try `qwen2.5` or `llama3.1`, which are reliable at tool calling.

### Extra — wire it into Claude Desktop

If you have [Claude Desktop](https://claude.ai/download), you can add your server there too, no `host.py` needed:

1. Open [`starter/claude_desktop_config.example.json`](starter/claude_desktop_config.example.json) and read the comments. Copy the `mcpServers` block into Claude Desktop's real config file (path is in the comment for your OS).
2. Set **both** absolute paths: `command` = the Python inside your venv (`where python` / `which python` with the venv active), `args` = the absolute path to your `server.py`.
3. **Fully restart Claude Desktop** (quit, not just close the window), then ask it something that needs a tool.

> If the server doesn't appear: the paths are almost always the problem. Use **absolute** paths and the venv's Python (not system Python), and check Claude Desktop's MCP log. A stdio server that `print()`s to stdout will also fail — that channel is reserved for the protocol.

## Going further

- **MCP Inspector** — the official debugging UI. With the venv active: `mcp dev server.py`, or `npx @modelcontextprotocol/inspector` (needs Node 22+). Click through your tools without any model.
- **Resources and prompts** — tools aren't the only thing a server exposes. Add a `@mcp.resource("...")` (read-only data the model can pull in) and a `@mcp.prompt()` (a reusable prompt template).
- **Go remote** — swap stdio for **Streamable HTTP** (`mcp run server.py --transport streamable-http`) so the server runs as a web service other machines can reach. This is how hosted MCP servers work.
- **A real integration** — expose a tool over an API you use (GitHub issues, the weather, a database). The weather server in the [official quickstart](https://modelcontextprotocol.io/docs/develop/build-server) is a great next build.

## Further reading

- [MCP: Build a server](https://modelcontextprotocol.io/docs/develop/build-server) — the official quickstart. **Check this for the current API** — it's the source of truth as the spec changes.
- [Model Context Protocol — Introduction](https://modelcontextprotocol.io/introduction) — what MCP is and why it exists.
- [Python SDK on GitHub](https://github.com/modelcontextprotocol/python-sdk) and [on PyPI](https://pypi.org/project/mcp/).
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — the debugging tool.
- [Protocol specification](https://modelcontextprotocol.io/specification) — the wire format, when you want to know what's actually being sent.

## Done? Make it count

Post your `python host.py "..."` output showing the model calling one of your tools (checkpoint 5) — or a Claude Desktop screenshot if you used that — in the module 03 thread on the Discord, to earn the module role.

---

## For facilitators

- **Re-verify against the live docs before every cohort.** This is the fastest-moving module in the set. Confirm the imports (`from mcp.server import MCPServer`, `from mcp import Client, StdioServerParameters`), `mcp.run(transport="stdio")`, and the `mcp dev` command still match, and bump the date/version note at the top. The whole starter is tested by running `python client.py` and the checkpoint snippets.
- Checkpoints 1–4 need **no** model, API key, or internet — they run entirely locally via `client.py`, so nobody is blocked by accounts or quotas. Checkpoint 5 is the payoff: the recommended path (Ollama + `host.py`) is also fully local and free, so a lab with no internet still works once models are pre-pulled. Groq is the fast cloud fallback; Claude Desktop is an optional extra.
- `host.py` was verified end-to-end against a local Ollama model. Expect small local models to need the text-JSON fallback it already includes; `qwen2.5`/`llama3.1` are the most reliable at native tool calls. Pre-pull the model you'll demo before the session — the first pull is a multi-GB download.
- The `print()`-breaks-stdio gotcha bites everyone at least once. Call it out early and show `logging` (writes to stderr) as the alternative.
- Demo could also be the MCP Inspector on the projector: `mcp dev server.py`, then click a tool, so the room sees the schema the SDK generated from the type hints.
- If `pip install mcp[cli]` resolves to a 1.x version on someone's machine, the `MCPServer` import fails (it was `FastMCP` in 1.x). The pin in `requirements.txt` (`>=2.0,<3.0`) prevents this; make sure they installed from it.
