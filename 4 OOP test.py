import unittest
from datetime import datetime
from user import User, UserService, UserUtil

class TestUser(unittest.TestCase):
    def test_get_details(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        user.email = "aijan.tilekova@example.com"
        self.assertEqual(user.get_details(), "User ID: 1\nName: Aijan Tilekova\nEmail: aijan.tilekova@example.com\nBirthday: 20/12/2005")

    def test_get_age(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        self.assertEqual(user.get_age(), datetime.today().year - 2005)

class TestUserService(unittest.TestCase):
    def test_add_user(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        UserService.add_user(user)
        self.assertEqual(len(UserService.users), 1)

    def test_find_user(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        UserService.add_user(user)
        found_user = UserService.find_user(1)
        self.assertEqual(found_user.name, "Aijan")

    def test_delete_user(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        UserService.add_user(user)
        UserService.delete_user(1)
        self.assertIsNone(UserService.find_user(1))

    def test_update_user(self):
        user = User(1, "Aijan", "Tilekova", datetime(2005, 12, 20))
        UserService.add_user(user)
        UserService.update_user(1, name="UpdatedName")
        self.assertEqual(UserService.find_user(1).name, "UpdatedName")

class TestUserUtil(unittest.TestCase):
    def test_generate_email(self):
        email = UserUtil.generate_email("Aijan", "Tilekova", "example.com")
        self.assertEqual(email, "aijan.tilekova@example.com")

    def test_is_strong_password(self):
        strong_password = "Aijan123!"
        weak_password = "12345"
        self.assertTrue(UserUtil.is_strong_password(strong_password))
        self.assertFalse(UserUtil.is_strong_password(weak_password))

    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(isinstance(user_id, int) and len(str(user_id)) == 9)

    def test_validate_email(self):
        valid_email = "aijan.tilekova@example.com"
        invalid_email = "aijan@tilekova@example"
        self.assertTrue(UserUtil.validate_email(valid_email))
        self.assertFalse(UserUtil.validate_email(invalid_email))

if __name__ == "__main__":
    unittest.main()
