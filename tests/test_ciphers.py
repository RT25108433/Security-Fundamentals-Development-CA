import unittest # Import the unittest module for testing
from caesar import encrypt, decrypt # Import the encrypt and decrypt functions from the caesar module


# Tests for the Caesar cipher functions
class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("Hello World", 3), "Khoor Zruog")

    def test_decrypt(self):
        self.assertEqual(decrypt("Khoor Zruog", 3), "Hello World")

    def test_encrypt_and_decrypt(self):
        original = "Hello World"
        encrypted = encrypt(original, 3)
        decrypted = decrypt(encrypted, 3)

        # Make sure the original message is recovered
        self.assertEqual(decrypted, original)

    def test_punctuation_and_numbers(self):
        # Punctuation and numbers should not be changed
        self.assertEqual(
            encrypt("Hello, World! 123", 3),
            "Khoor, Zruog! 123"
        )


if __name__ == "__main__":
    unittest.main()