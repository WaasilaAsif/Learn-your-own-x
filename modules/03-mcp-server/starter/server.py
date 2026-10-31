"""
Your MCP server. Runs on day one with one working tool (`add`); you add more
as you go through the checkpoints.

MCP (Model Context Protocol) is how an LLM reaches external tools. Your server
exposes functions; a client (the MCP Inspector, the test client in this folder,
or Claude Desktop) lists them and calls them. The model picks which to call.

Run it directly to check it starts (Ctrl-C to stop):
    python server.py
A stdio server waits silently for a client -- silence means it's working.

Verify with the test client in this folder:
    python client.py

Built against MCP Python SDK 2.x and protocol 2026-07-28. The spec moves fast --
if an import fails, check https://modelcontextprotocol.io/docs/develop/build-server
and https://pypi.org/project/mcp/ for the current API.
"""
from mcp.server import MCPServer

# The server. The name is how clients identify it.
mcp = MCPServer("learn-your-own-x")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b


# ---------------------------------------------------------------------------
# Checkpoint 2: add a tool here. The SDK reads your type hints and docstring to
# build the tool's schema automatically, so annotate the arguments and write a
# real docstring -- that text is what the model sees when deciding to call it.
#
# @mcp.tool()
# def word_count(text: str) -> int:
#     """Count the words in a piece of text."""
#     return len(text.split())
#
# Checkpoint 3: raise ToolError for bad input (see the README). Import it with:
#   from mcp.server.mcpserver.exceptions import ToolError
#
# Checkpoint 4: write a tool that reaches something external -- e.g. read and
# return the contents of a text file given its path. That "reaching out" is the
# whole reason MCP exists.
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    # stdio transport: the client launches this file as a subprocess and talks
    # over stdin/stdout. NEVER print() in a stdio server -- stdout carries the
    # JSON-RPC protocol and print() corrupts it. Use logging (writes to stderr).
    mcp.run(transport="stdio")
