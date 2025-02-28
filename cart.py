class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            print(f"Added {amount} x {device.name} to the cart.")
        else:
            print(f"Not enough stock for {device.name}. Only {device.stock} available.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if item[1] >= amount:
                    self.items.remove(item)
                    self.total_price -= device.price * amount
                    device.stock += amount
                    print(f"Removed {amount} x {device.name} from the cart.")
                else:
                    print(f"Cannot remove {amount} x {device.name}. Only {item[1]} in the cart.")
                return
        print(f"{device.name} not found in cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for item in self.items:
            print(f"{item[0].name} - Quantity: {item[1]}, Price: {item[0].price}, Total: {item[1] * item[0].price}")

    def checkout(self):
        print("Proceeding to checkout...")
        for item in self.items:
            print(f"{item[0].name} - Quantity: {item[1]}, Price: {item[0].price}, Total: {item[1] * item[0].price}")
        print(f"Total amount: {self.total_price}")
        self.items = []
        self.total_price = 0.0
        print("Thank you for your purchase!")
