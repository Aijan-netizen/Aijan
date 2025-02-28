# FIFTH ASSIGNMNET 
# Device Management System
This project allows users to manage different types of devices (smartphones, laptops, tablets) within a shopping cart system. Users can add, remove, view, and purchase devices from the cart.

## Overview
The program consists of the following components:
- **`Device`**: A base class representing a general device.
- **`Smartphone`, `Laptop`, `Tablet`**: Inheriting classes, each representing a specific type of device.
- **`Cart`**: Manages the shopping cart, allowing users to add, remove, and complete purchases.

## Features  
- **Add Device to Cart**: Users can add a device (smartphone, laptop, or tablet) to the cart.
- **Remove Device from Cart**: Users can remove a device from the cart.
- **Check Cart**: Displays the devices currently in the cart.
- **Purchase**: Finalize the purchase of all items in the cart, displaying the total cost.

## Class Descriptions  

### `Device` Class
A base class representing a general device.

- **Attributes**:
   - `name` (str): The device's name.
   - `brand` (str): The device's brand.
   - `price` (float): The device's price.
   - `category` (str): Device category (smartphone, laptop, tablet).

- **Methods**:
   - `__init__(self, name, brand, price, category)`: Initializes the device.
   - `get_device_info()`: Returns a string with the device's details.

### `Smartphone`, `Laptop`, `Tablet` Classes
Inheriting from `Device`, each class represents a specific device type.

- **Attributes**: Inherited from `Device`.
- **Methods**: 
   - `__init__(self, name, brand, price)`: Initializes the specific device with the provided details.

### `Cart` Class
Manages the shopping cart.

- **Attributes**:
   - `devices` (list): List of devices in the cart.

- **Methods**:
   - `add_device(self, device)`: Adds a device to the cart.
   - `remove_device(self, device)`: Removes a device from the cart.
   - `view_cart(self)`: Displays devices in the cart.
   - `checkout(self)`: Completes the purchase and shows the total cost.

## File Structure  

- **`device.py`**: Contains the `Device` class, the base class for devices.
- **`products.py`**: Contains the `Smartphone`, `Laptop`, and `Tablet` classes.
- **`cart.py`**: Contains the `Cart` class for managing the shopping cart.
- **`main.py`**: Main interface for interacting with the user.
- **`test.py`**: Contains tests to verify the classes' functionality.

## How It Works  
Users interact with the system through the following options:
1. **Add Device to Cart**: Add a specific device to the cart.
2. **Remove Device from Cart**: Remove a specific device from the cart.
3. **Check Cart**: View all devices currently in the cart.
4. **Complete Purchase**: Finalize the purchase and view the total amount.
5. **Exit**: Exit the program.

## Features Implemented  
- Developed a **`Device`** base class and device-specific subclasses: **`Smartphone`**, **`Laptop`**, **`Tablet`**.
- Created a **`Cart`** class for managing devices in the cart.
- Implemented user interaction options for managing devices and completing purchases.
