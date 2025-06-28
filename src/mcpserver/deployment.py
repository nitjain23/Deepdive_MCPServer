from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Package Demo")

@mcp.tool()
def addition(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b