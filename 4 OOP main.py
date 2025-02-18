from datetime import datetime
from user import User, UserService, UserUtil

# Example: Creating a user and interacting with the system
if __name__ == "__main__":
    user1 = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
    user1.email = "aijan.tilekova@example.com"
    print(user1.get_details())
    print(f"User age: {user1.get_age()}")

    # Add user to the service
    UserService.add_user(user1)
    print(f"Number of users: {UserService.get_number()}")

    # Generate email using UserUtil
    print(f"Generated email: {UserUtil.generate_email('Aijan', 'Tilekova', 'example.com')}")
