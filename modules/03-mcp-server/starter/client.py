"""
A tiny MCP client to test your server WITHOUT needing an LLM or any paid API.
It launches server.py as a subprocess, lists its tools, and optionally calls
one -- exactly what Claude Desktop does under the hood, minus the model.

List every tool the server exposes:
    python client.py

Call a tool by name with key=value arguments:
    python client.py add a=2 b=3
    python client.py word_count text="hello there world"

Arguments are sent as integers when they look like integers, else as strings.
Built against MCP Python SDK 2.x (`from mcp import Client`).
"""
import sys

import anyio
from mcp import Client, StdioServerParameters
from mcp.types import TextContent

# Launch server.py with the SAME Python running this client (works inside a venv).
server = StdioServerParameters(command=sys.executable, args=["server.py"])


def parse_arg(value: str):
    """Send ints as ints, floats as floats, everything else as a string."""
    for cast in (int, float):
        try:
            return cast(value)
        except ValueError:
            pass
    return value


async def main() -> None:
    call_name = sys.argv[1] if len(sys.argv) > 1 else None
    call_args = {}
    for pair in sys.argv[2:]:
        key, _, val = pair.partition("=")
        call_args[key] = parse_arg(val)

    async with Client(server) as client:
        tools = await client.list_tools()
        print(f"Server exposes {len(tools.tools)} tool(s):")
        for tool in tools.tools:
            print(f"  - {tool.name}: {tool.description}")

        if call_name:
            print(f"\nCalling {call_name}({call_args}) ...")
            result = await client.call_tool(call_name, call_args)
            if result.is_error:
                # A tool that raises ToolError comes back as an error RESULT,
                # not a Python exception -- check is_error, don't try/except.
                print("  tool reported an ERROR:")
            for block in result.content:
                if isinstance(block, TextContent):
                    print(f"  text: {block.text}")
            print(f"  structured: {result.structured_content}")


if __name__ == "__main__":
    anyio.run(main)
