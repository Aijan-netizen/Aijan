class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            return f"Added {amount} x {device.name} to cart."
        return f"Not enough stock for {device.name}."

    def remove_device(self, device, amount):
        for i, (item, qty) in enumerate(self.items):
            if item == device:
                if amount >= qty:
                    self.items.pop(i)
                    self.total_price -= item.price * qty
                else:
                    self.items[i] = (item, qty - amount)
                    self.total_price -= item.price * amount
                return f"Removed {amount} x {device.name} from cart."
        return f"{device.name} not found in cart."

    def get_total_price(self):
        return f"Total price: ${self.total_price:.2f}"

    def print_items(self):
        if not self.items:
            return "Cart is empty."
        return "\n".join([f"{qty} x {item.name} - ${item.price * qty:.2f}" for item, qty in self.items])

    def checkout(self):
        if not self.items:
            return "Cart is empty. Cannot proceed to checkout."
        receipt = "\n".join([f"{qty} x {item.name} - ${item.price * qty:.2f}" for item, qty in self.items])
        self.items.clear()
        total = self.total_price
        self.total_price = 0
        return f"Checkout successful!\n{receipt}\nTotal: ${total:.2f}"
