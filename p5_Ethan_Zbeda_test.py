"""Unit tests for p5_Ethan_Zbeda.py."""

import unittest

from p5_Ethan_Zbeda import (
    caesar_cipher,
    caesar_decipher,
    letter_frequency,
)


class TestCaesarCipher(unittest.TestCase):
    def test_cipher_preserves_case_and_nonletters(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_cipher_wraps_alphabet(self):
        self.assertEqual(caesar_cipher("xyz XYZ", 3), "abc ABC")

    def test_negative_and_large_shifts(self):
        self.assertEqual(caesar_cipher("Abc", -1), "Zab")
        self.assertEqual(caesar_cipher("Abc", 27), "Bcd")

    def test_decipher_restores_original_text(self):
        original = "Meet me at 8:00 PM."
        encrypted = caesar_cipher(original, 7)
        self.assertEqual(caesar_decipher(encrypted, 7), original)

    def test_letter_frequency_ignores_case_and_nonletters(self):
        frequencies = letter_frequency("Aa, bB! z7")
        self.assertEqual(frequencies["a"], 2)
        self.assertEqual(frequencies["b"], 2)
        self.assertEqual(frequencies["z"], 1)
        self.assertEqual(frequencies["c"], 0)
        self.assertEqual(len(frequencies), 26)

    def test_empty_text(self):
        self.assertEqual(caesar_cipher("", 5), "")
        self.assertTrue(all(count == 0 for count in letter_frequency("").values()))


if __name__ == "__main__":
    unittest.main()
