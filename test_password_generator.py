import unittest
from password_generator import generate_password

class PasswordGeneratorTests(unittest.TestCase):
    def test_generate_password_length(self):
        # Test generating password of length 8
        password = generate_password(8)
        self.assertEqual(len(password), 8)

        # Test generating password of length 12
        password = generate_password(12)
        self.assertEqual(len(password), 12)

        # Test generating password of length 20
        password = generate_password(20)
        self.assertEqual(len(password), 20)

    def test_generate_password_characters(self):
        # Test generating password with correct characters
        password = generate_password(10)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_generate_password_unique(self):
        # Test generating unique passwords
        password1 = generate_password(10)
        password2 = generate_password(10)
        self.assertNotEqual(password1, password2)

if __name__ == '__main__':
    unittest.main()
