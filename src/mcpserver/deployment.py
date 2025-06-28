from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Package Demo")

@mcp.tool()
def addition(a: int, b: int) -> int:
    """
    Adds two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b