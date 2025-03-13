from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class CalculatorWindow(QWidget):
    def __init__(self):
        """Initialize the calculator window and components."""
        super().__init__()
        
        self.calculator = Calculator()  # Instantiate the Calculator model
        self.init_ui()  # Set up the user interface

    def init_ui(self):
        """Set up the user interface with buttons and input field."""
        self.setWindowTitle('Calculator')

        # Create main layout and input field
        layout = QVBoxLayout()
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Create a grid for the buttons
        button_layout = QGridLayout()

        # Button labels
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3)
        ]

        # Add buttons to the grid layout
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_click)
            button_layout.addWidget(button, row, col)

        # Add clear button
        clear_button = QPushButton('C')
        clear_button.clicked.connect(self.on_clear_click)
        layout.addWidget(clear_button)

        # Add button layout to main layout
        layout.addLayout(button_layout)

        # Set layout of the window
        self.setLayout(layout)

    def on_button_click(self):
        """Handle button click events."""
        button = self.sender()  # Get the button that was clicked
        button_text = button.text()

        if button_text == "=":
            result = self.calculator.calculate()
            self.input_field.setText(str(result))  # Display the result in the input field
            self.calculator.clear_expression()  # Reset the calculator after calculation
        else:
            self.calculator.add_to_expression(button_text)
            self.input_field.setText(self.calculator.get_expression())  # Update the input field

    def on_clear_click(self):
        """Clear the input field and reset the expression."""
        self.calculator.clear_expression()
        self.input_field.clear()
