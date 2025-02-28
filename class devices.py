class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty
    def display_info(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months"
    def __str__(self):
        return self.display_info()
    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
    def is_available(self, amount):
        return self.stock >= amount
    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{super().__str__()}, Screen: {self.screen_size} inches, Battery: {self.battery_life} hours"
    def make_call(self):
        return f"Making a call from {self.name}..."
    def install_app(self):
        return f"Installing app on {self.name}..."


class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()}, RAM: {self.ram_size}GB, CPU: {self.processor_speed}GHz"
    def run_program(self):
        return f"Running program on {self.name}..."
    def use_keyboard(self):
        return f"Typing on {self.name}..."


class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Resolution: {self.screen_resolution}, Weight: {self.weight}g"
    def browse_internet(self):
        return f"Browsing internet on {self.name}..."
    def use_touchscreen(self):
        return f"Using touchscreen on {self.name}..."
