from calculator import Calculator
from view import CalculatorWindow

class Controller:
    def __init__(self):
        """Initialize the controller with a calculator instance and the window."""
        self.calculator = Calculator()  
        self.window = CalculatorWindow(self.calculator)  
        self.connect_signals()  # Connect signals when controller is initialized

    def connect_signals(self):
        """Connect signals for interaction with the window and calculator."""
        self.window.digit_button_clicked.connect(self.on_button_click)
        self.window.operator_button_clicked.connect(self.on_button_click)
        self.window.clear_button_clicked.connect(self.on_clear)
        self.window.equals_button_clicked.connect(self.on_equals)

    def show(self):
        """Display the calculator window."""
        self.window.show()

    def on_button_click(self, char):
        """Handle the button click event."""
        self.calculator.add_to_expression(char)
        self.update_display()

    def on_clear(self):
        """Clear the input field and expression."""
        self.calculator.clear_expression()
        self.update_display()

    def on_equals(self):
        """Calculate the result of the expression."""
        result = self.calculator.calculate()
        self.window.update_input_field(str(result))
        self.window.add_to_history(f"{self.calculator.get_expression()} = {result}")

    def update_display(self):
        """Update the input field with the current expression."""
        self.window.update_input_field(self.calculator.get_expression())
