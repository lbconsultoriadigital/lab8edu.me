import unittest

from main import calculate_expression, execute_tool


class CalculateExpressionTests(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(calculate_expression("15 * 4 + 10"), "70")

    def test_parentheses_and_unary_operator(self):
        self.assertEqual(calculate_expression("-(8 + 2) / 5"), "-2.0")

    def test_rejects_names_and_function_calls(self):
        self.assertTrue(calculate_expression("open('secret')").startswith("Error:"))

    def test_rejects_unsupported_power_operator(self):
        self.assertTrue(calculate_expression("9 ** 9").startswith("Error:"))

    def test_handles_division_by_zero(self):
        self.assertTrue(calculate_expression("1 / 0").startswith("Error:"))

    def test_unknown_tool(self):
        self.assertEqual(
            execute_tool("missing_tool"),
            "Error: Tool 'missing_tool' not found.",
        )


if __name__ == "__main__":
    unittest.main()
