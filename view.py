from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

class CalculatorWindow(QWidget):
    digit_button_clicked = pyqtSignal(str)
    operator_button_clicked = pyqtSignal(str)
    clear_button_clicked = pyqtSignal()
    equals_button_clicked = pyqtSignal()

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
            if text in '0123456789': 
                button.clicked.connect(lambda _, b=text: self.digit_button_clicked.emit(b))
            elif text in '+-*/':  
                button.clicked.connect(lambda _, b=text: self.operator_button_clicked.emit(b))
            elif text == '=': 
                button.clicked.connect(self.equals_button_clicked.emit)
            button_layout.addWidget(button, row, col)

        clear_button = QPushButton('C')
        clear_button.setStyleSheet("font-size: 20px; height: 50px;")
        clear_button.clicked.connect(self.clear_button_clicked.emit)
        button_layout.addWidget(clear_button, 4, 0, 1, 4) 

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def update_input_field(self, text):
        """Update the input field with new text."""
        self.input_field.setText(text)

    def add_to_history(self, entry):
        """Optional method to add calculations to history."""
        print(f"History: {entry}")
