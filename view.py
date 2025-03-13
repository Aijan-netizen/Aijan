from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class CalculatorWindow(QWidget):
    def __init__(self, calculator):
        """Initialize the calculator window and components."""
        super().__init__()
        self.calculator = calculator
        self.init_ui()

    def init_ui(self):
        """Set up the user interface with buttons and input field."""
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400) 

        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setReadOnly(True)  
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignRight)  
        self.input_field.setStyleSheet("font-size: 20px; height: 40px;")  
        layout.addWidget(self.input_field)

        button_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3), ]

        self.buttons = {} 
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 20px; height: 50px;")
            self.buttons[text] = button  
            button.clicked.connect(lambda _, b=text: self.on_button_click(b))  
            button_layout.addWidget(button, row, col)

        clear_button = QPushButton('C')
        clear_button.setStyleSheet("font-size: 20px; height: 50px;")
        clear_button.clicked.connect(self.on_clear)
        button_layout.addWidget(clear_button, 4, 0, 1, 4)  

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def on_button_click(self, char):
        """Add character to the current expression."""
        self.calculator.add_to_expression(char)
        self.input_field.setText(self.calculator.get_expression())

    def on_clear(self):
        """Clear the input field and expression."""
        self.calculator.clear_expression()
        self.input_field.clear()
