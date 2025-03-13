from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from model import Calculator
from view import CalculatorWindow

class CalculatorController:
    def __init__(self):
        self.calculator = Calculator()  # Create a calculator object
        self.window = CalculatorWindow(self.calculator)  # Pass calculator to the window
        self.setup()

    def setup(self):
        # Add event handlers for the buttons
        self.window.button0.clicked.connect(lambda: self.on_button_click('0'))
        self.window.button1.clicked.connect(lambda: self.on_button_click('1'))
        self.window.button2.clicked.connect(lambda: self.on_button_click('2'))
        self.window.button3.clicked.connect(lambda: self.on_button_click('3'))
        self.window.button4.clicked.connect(lambda: self.on_button_click('4'))
        self.window.button5.clicked.connect(lambda: self.on_button_click('5'))
        self.window.button6.clicked.connect(lambda: self.on_button_click('6'))
        self.window.button7.clicked.connect(lambda: self.on_button_click('7'))
        self.window.button8.clicked.connect(lambda: self.on_button_click('8'))
        self.window.button9.clicked.connect(lambda: self.on_button_click('9'))
        self.window.button_plus.clicked.connect(lambda: self.on_operator_click('+'))
        self.window.button_minus.clicked.connect(lambda: self.on_operator_click('-'))
        self.window.button_mul.clicked.connect(lambda: self.on_operator_click('*'))
        self.window.button_div.clicked.connect(lambda: self.on_operator_click('/'))
        self.window.button_clear.clicked.connect(self.on_clear)
        self.window.button_equals.clicked.connect(self.on_equals)

    def on_button_click(self, char):
        """Add a character to the calculator's expression"""
        self.calculator.add_to_expression(char)
        self.window.input.setText(self.calculator.get_expression())

    def on_operator_click(self, operator):
        """Add an operator to the calculator's expression"""
        self.calculator.add_to_expression(operator)
        self.window.input.setText(self.calculator.get_expression())

    def on_clear(self):
        """Clear the calculator's expression"""
        self.calculator.clear_expression()
        self.window.input.clear()

    def on_equals(self):
        """Calculate the result of the expression"""
        result = self.calculator.calculate()
        self.window.input.setText(str(result))

if __name__ == '__main__':
    app = QApplication([])
    controller = CalculatorController()
    controller.window.show()
    app.exec_()
