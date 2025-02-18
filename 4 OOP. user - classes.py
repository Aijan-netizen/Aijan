from datetime import datetime
import random
import string

# User Class
class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = None
        self.password = None
        self.birthday = birthday

    def get_details(self):
        return f"User ID: {self.user_id}\nName: {self.name} {self.surname}\nEmail: {self.email}\nBirthday: {self.birthday.strftime('%d/%m/%Y')}"

    def get_age(self):
        return datetime.today().year - self.birthday.year

# UserService Class
class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id] = user_update

    @classmethod
    def get_number(cls):
        return len(cls.users)

# UserUtil Class
class UserUtil:
    @staticmethod
    def generate_user_id():
        return int(f"{datetime.today().year % 100}{random.randint(1000000, 9999999)}")

    @staticmethod
    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
        return password

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in string.punctuation for c in password):
            return False
        return True

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        import re
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None
