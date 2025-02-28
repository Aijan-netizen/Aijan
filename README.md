# 4TH ASSIGNMENT  
# User Management System  

## Overview  
This Python project provides an object-oriented solution for managing user records. It includes three primary classes:  
- `User`: Represents an individual user.  
- `UserService`: Manages multiple users.  
- `UserUtil`: Provides utility functions for user creation and validation.  

## Features  
The system allows you to:  
- Create and manage user accounts.  
- Store user details such as name, surname, email, password, and birthday.  
- Perform operations such as adding, updating, deleting, and retrieving users.  
- Generate secure passwords and validate emails.  

---  

## 🔹 User Class  
### Attributes:  
- `user_id` (int) – Unique identifier for the user.  
- `name` (str) – First name of the user.  
- `surname` (str) – Last name of the user.  
- `email` (str) – Email address of the user.  
- `password` (str) – Secure password of the user.  
- `birthday` (datetime) – Date of birth of the user.  

### Methods:  
- `__init__(self, user_id, name, surname, birthday)`: Initializes a user with given details.  
- `get_details(self) -> str`: Returns a formatted string containing user details.  
- `get_age(self) -> int`: Calculates the user's age based on the current year. Month and day are not considered for accuracy.

---

## 🔹 UserService Class
### Class Attribute:
- `users (dict)`: Stores all user objects, where the key is `user_id`, and the value is the corresponding `User` object.

### Class Methods:
- `add_user(cls, user: User)`: Adds a user to the system.  
- `find_user(cls, user_id: int) -> User | None`: Finds and returns a user by their `user_id`.  
- `delete_user(cls, user_id: int)`: Removes a user from the system.  
- `update_user(cls, user_id: int, **kwargs)`: Updates a user’s attributes by passing keyword arguments.  
- `get_number(cls) -> int`: Returns the total number of users.

---

## 🔹 UserUtil Class  
### Static Methods:  
- `generate_user_id() -> int`: Generates a unique user ID with 9 digits. The first two digits correspond to the current year.  
- `generate_password() -> str`: Generates a strong password (at least 8 characters, including uppercase, lowercase, digits, and special characters).  
- `is_strong_password(password: str) -> bool`: Checks whether a password meets security requirements.  
- `generate_email(name: str, surname: str, domain: str) -> str`: Creates an email address from the user’s name and surname.  
- `validate_email(email: str) -> bool`: Verifies if an email address is in a valid format.

---  

## ✅ What Has Been Done  
- Implemented `User`, `UserService`, and `UserUtil` classes.  
- Added methods for user management.  
- Implemented password and email validation.  
- Created test cases.  
- Provided sample input/output examples.  
- Included UML class diagram.

---
