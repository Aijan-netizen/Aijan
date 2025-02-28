from device import Device
from products import Smartphone, Laptop, Tablet
from cart import Cart

def test_device_class():
    device = Device("Generic Device", 1000, 10, 12)
    assert device.name == "Generic Device"
    assert device.price == 1000
    assert device.stock == 10
    assert device.warranty_period == 12

def test_smartphone_class():
    phone = Smartphone("iPhone 13", 999, 10, 24, 6.1, 20)
    assert phone.screen_size == 6.1
    assert phone.battery_life == 20
    assert phone.name == "iPhone 13"

def test_cart_class():
    cart = Cart()
    phone = Smartphone("iPhone 13", 999, 10, 24, 6.1, 20)
    cart.add_device(phone, 2)
    assert cart.get_total_price() == 1998
    cart.remove_device(phone, 1)
    assert cart.get_total_price() == 999

def run_tests():
    test_device_class()
    test_smartphone_class()
    test_cart_class()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
