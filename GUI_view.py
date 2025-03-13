from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

class CalculatorWindow(QWidget):
    def __init__(self, calculator):
        """Initialize the calculator window and components."""
        super().__init__()
        self.calculator = calculator
        self.init_ui()

    def init_ui(self):
        """Set up the user interface with buttons and input field."""
        self.setWindowTitle('Calculator')

        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setReadOnly(True)  
        layout.addWidget(self.input_field)

        button_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),  ]

        self.buttons = {} 
        for (text, row, col) in buttons:
            button = QPushButton(text)
            self.buttons[text] = button  
            button_layout.addWidget(button, row, col)

        clear_button = QPushButton('C')
        self.buttons['C'] = clear_button
        button_layout.addWidget(clear_button, 4, 0, 1, 4)

        layout.addLayout(button_layout)
        self.setLayout(layout)
