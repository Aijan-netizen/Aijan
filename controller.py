from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt

class Controller:
    def __init__(self):
        self.calculator = Calculator()  # Create a Calculator instance
        self.window = QWidget()
        self.setup_ui()

    def setup_ui(self):
        self.window.setWindowTitle("Calculator")

        layout = QVBoxLayout()
        self.input_field = QLineEdit(self.window)
        layout.addWidget(self.input_field)

        button_layout = QVBoxLayout()

        buttons = [
            ('7', self.on_button_click), ('8', self.on_button_click), ('9', self.on_button_click), ('/', self.on_button_click),
            ('4', self.on_button_click), ('5', self.on_button_click), ('6', self.on_button_click), ('*', self.on_button_click),
            ('1', self.on_button_click), ('2', self.on_button_click), ('3', self.on_button_click), ('-', self.on_button_click),
            ('0', self.on_button_click), ('.', self.on_button_click), ('+', self.on_button_click), ('=', self.on_equals)
        ]

        for text, func in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda _, b=text: func(b))
            button_layout.addWidget(button)

        clear_button = QPushButton('C')
        clear_button.clicked.connect(self.on_clear)
        button_layout.addWidget(clear_button)

        self.history_list = QListWidget(self.window)
        layout.addWidget(self.history_list)
        layout.addLayout(button_layout)
        self.window.setLayout(layout)

        self.window.setFocusPolicy(Qt.StrongFocus)

    def on_button_click(self, char):
        """Add character to the current expression."""
        self.calculator.add_to_expression(char)
        self.input_field.setText(self.calculator.get_expression())

    def on_clear(self):
        """Clear the input field and expression."""
        self.calculator.clear_expression()
        self.input_field.clear()

    def on_equals(self, _):
        """Calculate the result of the expression."""
        result = self.calculator.calculate()
        self.input_field.setText(str(result))
        self.history_list.addItem(f"{self.calculator.get_expression()} = {result}")

    def show(self):
        self.window.show()

if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    controller.show()
    app.exec_()
