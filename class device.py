class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months")

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months"

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False

