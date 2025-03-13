class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        """Add a character (digit or operator) to the current expression."""
        self.expression += char

    def remove_last_character(self):
        """Remove the last character from the current expression."""
        self.expression = self.expression[:-1]

    def clear_expression(self):
        """Clear the current expression."""
        self.expression = ""

    def calculate(self):
        """Evaluate the current mathematical expression and return the result."""
        try:
            if "/0" in self.expression:  
                return "Error: Division by zero"
            
            result = eval(self.expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {str(e)}"  

    def get_expression(self):
        """Return the current mathematical expression."""
        return self.expression
