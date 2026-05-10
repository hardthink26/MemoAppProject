import unittest

from app import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(username="u1")
        u.password = "cat"
        self.assertIsNotNone(u.password_hash)

    def test_no_password_getter(self):
        u = User(username="u1")
        u.password = "cat"
        with self.assertRaises(AttributeError):
            _ = u.password

    def test_password_verification(self):
        u = User(username="u1")
        u.password = "cat"
        self.assertTrue(u.verify_password("cat"))
        self.assertFalse(u.verify_password("dog"))

    def test_password_salts_are_random(self):
        u = User(username="u1")
        u.password = "cat"
        u2 = User(username="u2")
        u2.password = "cat"
        self.assertNotEqual(u.password_hash, u2.password_hash)


if __name__ == "__main__":
    unittest.main()
