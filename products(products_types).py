from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{self.name} (Smartphone) - Price: {self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months, Screen: {self.screen_size} inches, Battery Life: {self.battery_life} hours"

    def make_call(self):
        return f"Making a call with {self.name}..."

    def install_app(self):
        return f"Installing an app on {self.name}..."

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{self.name} (Laptop) - Price: {self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months, RAM: {self.ram_size}GB, Processor: {self.processor_speed}GHz"

    def run_program(self):
        return f"Running a program on {self.name}..."

    def use_keyboard(self):
        return f"Typing on {self.name}'s keyboard..."

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_resolution, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{self.name} (Tablet) - Price: {self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months, Resolution: {self.screen_resolution}, Weight: {self.weight} grams"

    def browse_internet(self):
        return f"Browsing the internet on {self.name}..."

    def use_touchscreen(self):
        return f"Using the touchscreen on {self.name}..."

