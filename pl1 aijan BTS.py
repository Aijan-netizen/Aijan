# user.py
def get_user_info():
    user_info = {}
    user_info["name"] = input("What is the user's name? \n")
    user_info["age"] = input("What is the user's age? \n")
    user_info["country_of_birth"] = input("What is the user's country of birth? \n")
    user_info["known_for"] = input("What is the user known for? \n")
    return user_info
def display_user_info(user_info):
    print("\nUser Information:")
    print(f"Name: {user_info['name']}")
    print(f"Age: {user_info['age']}")
    print(f"Country of Birth: {user_info['country_of_birth']}")
    print(f"Known for: {user_info['known_for']}")

if __name__ == "__main__":
    user_info = get_user_info()
    display_user_info(user_info)
