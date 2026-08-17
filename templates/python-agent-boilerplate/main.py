"""
LAB8 - Minimal ReAct Agent Boilerplate with Tool Calling
Demonstrates structured tool execution, observation handling, and loop termination.
"""

import os
import json

# Simulated Tool Registry
def get_current_weather(location: str) -> str:
    """Returns weather information for a given city."""
    return f"The weather in {location} is sunny and 24°C."

def calculate_expression(expression: str) -> str:
    """Safely calculates a mathematical expression."""
    try:
        # Simple restricted eval for demonstration
        allowed_chars = set("0123456789+-*/(). ")
        if all(c in allowed_chars for c in expression):
            return str(eval(expression, {"__builtins__": None}, {}))
        return "Error: Invalid characters in expression."
    except Exception as e:
        return f"Error: {str(e)}"

TOOLS = {
    "get_current_weather": get_current_weather,
    "calculate_expression": calculate_expression,
}

def execute_tool(tool_name: str, **kwargs) -> str:
    """Executes a tool from the registry."""
    if tool_name in TOOLS:
        return TOOLS[tool_name](**kwargs)
    return f"Error: Tool '{tool_name}' not found."

def main():
    print("--- LAB8 Python Agent Boilerplate ---")
    print("Testing tool: calculate_expression(expression='15 * 4 + 10')")
    res1 = execute_tool("calculate_expression", expression="15 * 4 + 10")
    print(f"Result: {res1}")
    print()
    print("Testing tool: get_current_weather(location='São Paulo')")
    res2 = execute_tool("get_current_weather", location="São Paulo")
    print(f"Result: {res2}")

if __name__ == "__main__":
    main()
