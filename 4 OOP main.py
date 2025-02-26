from datetime import datetime
from user import User, UserService, UserUtil
if __name__ == "__main__":
    # Creating a user
    user1 = User(UserUtil.generate_user_id(), "Aijan", "Tilekova", datetime(2005, 12, 20))
    user1.email = UserUtil.generate_email(user1.name, user1.surname, "example.com")
    user1.password = UserUtil.generate_password()

    print(user1.get_details())
    print(f"User age: {user1.get_age()}")

    # Add user to the service
    UserService.add_user(user1)
    print(f"Number of users: {UserService.get_number()}")

    # Validate email
    print(f"Is email valid? {UserUtil.validate_email(user1.email)}")

    # Generate and check password strength
    new_password = UserUtil.generate_password()
    print(f"Generated strong password: {new_password}")
    print(f"Is password strong? {UserUtil.is_strong_password(new_password)}")
