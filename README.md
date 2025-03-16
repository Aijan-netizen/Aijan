# SEVENTH ASSIGNMENT 
# Calculator Application

This project implements a simple graphical calculator using **PyQt5**. The application handles basic arithmetic operations such as addition, subtraction, multiplication, and division. It follows the **Model-View-Controller** (MVC) design pattern, consisting of multiple components: the **model** (Calculator class), **controller** (Controller class), and **view** (CalculatorWindow class).

## Project Structure

The project consists of four main files:

1. **`main.py`** - The entry point for the application. It initializes and runs the PyQt application.
2. **`calculator.py`** - The model that performs the actual calculations.
3. **`controller.py`** - The controller that connects the model and view, handling user input and triggering calculations.
4. **`view.py`** - The view that defines the graphical user interface (GUI) for the calculator.

---

## How It Works

### 🔹 Application Flow:
- The `main.py` file starts the application by initializing a `QApplication` instance and displaying the calculator window.
- The `Controller` class acts as an intermediary between the user interface (`view.py`) and the calculation logic (`calculator.py`).
- The `Calculator` class in `calculator.py` manages the mathematical expressions, performs calculations, and keeps track of the entered data.
- The `CalculatorWindow` class in `view.py` displays the interface, handles button clicks, and shows the results to the user.

### 🔹 Features:
- **Basic arithmetic operations**: Addition, subtraction, multiplication, and division.
- **Clear functionality**: Resets the current expression.
- **History**: Displays the past calculations and results.
- **Smooth scrolling**: The history list scrolls smoothly when a new entry is added.

---
### 🔹 Calculator UI:
- Input Field: Displays the current expression or result.
- History List: Shows the list of previous calculations.
- Buttons: Numeric buttons `(0-9)`, decimal point `(.)`, arithmetic operators `(+, -, *, /)`, equals button `(=)`, and a clear button `(C)`.

---
### Examples

![My Image](images/Снимок.png)

---
## What I Have Done
 - Created the `Calculator` class to manage mathematical operations, expression handling, and evaluation.
 - Created the `Controller` class to link the calculator logic with the view. It handles button clicks and updates the display.
 - Designed the `CalculatorWindow` class to define the user interface (buttons, input field, history list) using PyQt5.
 - Implemented event-driven programming: The controller responds to user inputs (button clicks) and updates the display accordingly.
 - Smooth scrolling for history: When a new calculation is added, the history list scrolls smoothly to show the latest result.

---
## Tools and Libraries Used
- Python 3.x — The primary programming language used for developing the application.
- PyQt5 — The library used for creating the graphical user interface (GUI).
- Qt Designer — A tool for designing user interfaces, used alongside PyQt5.
- VS Code — The text editor used for writing and editing the code.
- Pip — The package manager used for installing dependencies (e.g., PyQt5).
- Git — The version control system used for managing the repository.
