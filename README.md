# FIFTH ASSIGNMENT 
# Device Management System
This project allows users to manage different types of devices (smartphones, laptops, tablets) and interact with a shopping cart system. It enables users to add, remove, and purchase devices from the cart.

## Overview  
The program consists of the following main components:
- **`Device`**: A base class representing a general device.
- **`Smartphone`, `Laptop`, `Tablet`**: Classes inheriting from `Device`, representing specific types of devices.
- **`Cart`**: A class for managing a shopping cart, including adding, removing, and completing purchases.

## Features  
- **Add Device to Cart**: Add a specific device (smartphone, laptop, or tablet) to the cart.
- **Remove Device from Cart**: Remove a device from the cart.
- **Check Cart**: Display the devices currently in the cart.
- **Purchase**: Complete the purchase of all items in the cart.

## Class Descriptions  

### `Device` Class
This is the base class representing a general device.

- **Attributes**:
   - `name` (str): The name of the device.
   - `brand` (str): The brand of the device.
   - `price` (float): The price of the device.
   - `category` (str): The category of the device (e.g., smartphone, laptop, tablet).

- **Methods**:
   - `__init__(self, name, brand, price, category)`: Initializes a device with the given name, brand, price, and category.
   - `get_device_info()`: Returns a string containing the device's details (name, brand, price, category).

### `Smartphone`, `Laptop`, `Tablet` Classes
These are subclasses of `Device`, each representing a specific type of device.

- **Attributes** (inherited from `Device`):
   - `name`, `brand`, `price`, `category`.

- **Methods**:
   - `__init__(self, name, brand, price)`: Initializes the specific device type with the provided name, brand, and price.

### `Cart` Class
This class manages the shopping cart, allowing users to add, remove, and view devices.

- **Attributes**:
   - `devices` (list): A list that stores the devices in the cart.

- **Methods**:
   - `add_device(self, device)`: Adds a device to the cart.
   - `remove_device(self, device)`: Removes a device from the cart.
   - `view_cart(self)`: Displays all devices currently in the cart.
   - `checkout(self)`: Completes the purchase, displaying the total cost and confirming the transaction.

## File Structure  
The project contains the following files:

- **`device.py`**: Contains the base class `Device`, which is inherited by the specific device classes.
- **`products.py`**: Contains the device classes: `Smartphone`, `Laptop`, `Tablet`.
- **`cart.py`**: The `Cart` class, with methods for adding, removing, and completing purchases.
- **`main.py`**: The main interface for interacting with the user.
- **`test.py`**: Contains tests to ensure the correctness of the classes.

## How It Works  
The user interacts with the system through the following options:

1. **Add Device to Cart**: Add a smartphone, laptop, or tablet to the shopping cart.
2. **Remove Device from Cart**: Remove a specific device from the cart.
3. **Check Cart**: Display the devices currently in the cart.
4. **Complete Purchase**: Finalize the purchase and display the total amount.
5. **Exit**: Exit the program.

## Features Implemented
- Created the `Device` class as the base class for all device types.
- Implemented the `Smartphone`, `Laptop`, and `Tablet` classes, inheriting from `Device`.
- Developed the `Cart` class for managing a shopping cart, with the ability to add, remove, and check devices in the cart.
- Implemented basic user interaction with options to manage devices and purchase.
