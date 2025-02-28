from products import Smartphone, Laptop, Tablet
from cart import Cart

def show_devices(devices):
    print("Available Devices:")
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device}")

def main():
    # Create some devices
    devices = [
        Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
        Smartphone("Samsung Galaxy S21", 799, 15, 12, 6.2, 22),
        Laptop("MacBook Pro", 1999, 5, 24, 16, 3.1),
        Laptop("Dell XPS 13", 1499, 8, 12, 8, 2.8),
        Tablet("iPad Pro", 1099, 12, 12, "2732x2048", 460),
        Tablet("Samsung Galaxy Tab", 499, 20, 12, "1920x1200", 340)
    ]

    cart = Cart()

    while True:
        print("\n1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_devices(devices)
            device_choice = int(input("Enter the number of the device you want to add to your cart: ")) - 1
            amount = int(input("Enter the quantity: "))
            if 0 <= device_choice < len(devices):
                cart.add_device(devices[device_choice], amount)
            else:
                print("Invalid choice.")
        
        elif choice == '2':
            cart.print_items()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
