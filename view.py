from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QListWidget
from functools import partial

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
        self.setGeometry(100, 100, 300, 500)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setReadOnly(True)
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_field.setStyleSheet("font-size: 20px; height: 40px; background: #1C1C1C; color: white;")
        layout.addWidget(self.input_field)

        self.history_list = QListWidget(self)
        self.history_list.setStyleSheet("font-size: 14px; height: 100px; background: #1C1C1C; color: lightgray;")
        self.history_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        layout.addWidget(self.history_list)

        button_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),]

        self.buttons = {}
        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setStyleSheet(
                "font-size: 20px; height: 50px; background: #4A4A4A; color: white; border: 1px solid #5E5E5E; border-radius: 5px;")
            self.buttons[text] = button
            if text in '0123456789.':
                button.clicked.connect(partial(self.digit_button_clicked.emit, text))
            elif text in '+-*/':
                button.clicked.connect(partial(self.operator_button_clicked.emit, text))
            elif text == '=':
                button.clicked.connect(self.equals_button_clicked.emit)
            button_layout.addWidget(button, row, col)

        clear_button = QPushButton('C')
        clear_button.setStyleSheet(
            "font-size: 20px; height: 50px; background: #FF6347; color: white; border: none; border-radius: 5px;")
        clear_button.clicked.connect(self.clear_button_clicked.emit)
        button_layout.addWidget(clear_button, 4, 0, 1, 4)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.smooth_scroll)

        self.target_scroll_value = 0  

    def update_input_field(self, text):
        """Update the input field with new text."""
        self.input_field.setText(text)

    def add_to_history(self, entry):
        """Add calculations to the history list."""
        self.history_list.addItem(entry)

        self.target_scroll_value = self.history_list.verticalScrollBar().maximum()
        self.scroll_timer.start(10)

    def smooth_scroll(self):
        """Smoothly scroll to the end of the list."""
        current_value = self.history_list.verticalScrollBar().value()

        if current_value < self.target_scroll_value:
            self.history_list.verticalScrollBar().setValue(current_value + 1)
        else:
            self.scroll_timer.stop()
