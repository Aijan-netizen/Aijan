class Calculator:
    def __init__(self):
        self.expression = ""  # храним текущее выражение

    def add_to_expression(self, char: str):
        self.expression += char  # добавляем символ в выражение

    def remove_last_character(self):
        self.expression = self.expression[:-1]  # удаляем последний символ

    def clear_expression(self):
        self.expression = ""  # очищаем выражение

    def calculate(self):
        try:
            return eval(self.expression)  # вычисляем выражение
        except Exception as e:
            return f"Ошибка: {str(e)}"  # если ошибка, выводим сообщение

    def get_expression(self):
        return self.expression  # возвращаем текущее выражение
