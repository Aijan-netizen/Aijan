import ast
class Calculator:
    def __init__(self, expression=""):
        self.expression = expression

    def add_to_expression(self, char):
        self.expression += str(char)

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = self.safe_eval(self.expression)
            return result
        except Exception as e:
            return "Error"

    def get_expression(self):
        return self.expression

    def safe_eval(self, expr):
        """Safely evaluate mathematical expressions."""
        try:
            return eval(compile(ast.parse(expr, mode='eval'), '<string>', 'eval'))
        except Exception as e:
            return "Error"
