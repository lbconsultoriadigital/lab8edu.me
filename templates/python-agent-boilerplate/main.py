"""
LAB8 - Minimal ReAct Agent Boilerplate with Tool Calling
Demonstrates structured tool execution, observation handling, and loop termination.
"""

import ast
import math
import operator

MAX_EXPRESSION_LENGTH = 100
MAX_ABS_RESULT = 1_000_000_000_000

BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def get_current_weather(location: str) -> str:
    """Returns simulated weather information for a given city."""
    return f"The weather in {location} is sunny and 24°C."


def _evaluate_math_node(node: ast.AST) -> int | float:
    """Evaluates a small, explicit subset of Python's math syntax."""
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ):
        value = node.value
    elif isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        left = _evaluate_math_node(node.left)
        right = _evaluate_math_node(node.right)
        value = BINARY_OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        value = UNARY_OPERATORS[type(node.op)](_evaluate_math_node(node.operand))
    else:
        raise ValueError("Only numbers, parentheses, +, -, *, and / are allowed.")

    if not math.isfinite(value) or abs(value) > MAX_ABS_RESULT:
        raise ValueError("Result is outside the allowed range.")
    return value


def calculate_expression(expression: str) -> str:
    """Safely calculates a limited arithmetic expression without eval()."""
    try:
        if not expression or len(expression) > MAX_EXPRESSION_LENGTH:
            raise ValueError("Expression must contain between 1 and 100 characters.")
        parsed = ast.parse(expression, mode="eval")
        return str(_evaluate_math_node(parsed.body))
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError, OverflowError) as error:
        return f"Error: {error}"

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
