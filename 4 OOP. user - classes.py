import random
import re
import string
from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = None
        self.password = None

    def get_details(self):
        return f"User ID: {self.user_id}\nName: {self.name} {self.surname}\nEmail: {self.email}\nBirthday: {self.birthday.strftime('%d/%m/%Y')}"

    def get_age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, **kwargs):
        user = cls.find_user(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)

    @classmethod
    def get_number(cls):
        return len(cls.users)

class UserUtil:
    @staticmethod
    def generate_user_id():
        year = str(datetime.today().year)[2:]  # Take last two digits of the year
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(year + random_digits)

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$"
        return bool(re.match(pattern, email))
