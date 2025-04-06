from mcp.server.fastmcp import FastMCP


mcp = FastMCP("HelloMCP")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.prompt()
def translation_ja(txt: str) -> str:
    """Translating to Japanese"""
    return f"Please translate this sentence into Japanese:\n\n{txt}"
