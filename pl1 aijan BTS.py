def get_user_info():
    user_info = {   
        "name": input("What is the user's name? \n"),
        "age": input("What is the user's age? \n"),
        "country_of_birth": input("What is the user's country of birth? \n"),
        "known_for": input("What is the user known for? \n") }
    return user_info

def display_user_info(user_info):
    print("\nUser Information:")
    print("Name:", user_info["name"])
    print("Age:", user_info["age"])
    print("Country of Birth:", user_info["country_of_birth"])
    print("Known for:", user_info["known_for"])

user_info = get_user_info()
display_user_info(user_info) 
