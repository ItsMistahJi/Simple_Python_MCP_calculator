from mcp.server.fastmcp import FastMCP
import math

# Instantiate the MCP server client
mcp = FastMCP("Hello World")

# Define tools

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return float(a / b)

@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    return int(a ** b)

@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    return float(a ** 0.5)

@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    return float(a ** (1/3))

@mcp.tool()
def factorial(a: int) -> int:
    """Factorial of a number"""
    return int(math.factorial(a))

@mcp.tool()
def log(a: int) -> float:
    """Log of a number"""
    return float(math.log(a))

@mcp.tool()
def remainder(a: int, b: int) -> int:
    """Remainder of two numbers division"""
    return int(a % b)

@mcp.tool()
def sin(a: int) -> float:
    """Sine of a number"""
    return float(math.sin(a))

@mcp.tool()
def cos(a: int) -> float:
    """Cosine of a number"""
    return float(math.cos(a))

@mcp.tool()
def tan(a: int) -> float:
    """Tangent of a number"""
    return float(math.tan(a))

# Define resources

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")