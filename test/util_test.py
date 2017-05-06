import unittest
from util import get_digits, get_int_from_digits, is_palindromic


class TestDigitMethods(unittest.TestCase):

    def test_get_digits(self):
        self.assertEqual(
            get_digits(1232, 10),
            [1, 2, 3, 2])
        self.assertEqual(
            get_digits(0b10010101, 2),
            [1, 0, 0, 1, 0, 1, 0, 1])

    def test_get_int_from_digits(self):
        self.assertEqual(
            get_int_from_digits([4, 5, 3, 9, 0]),
            45390)
        self.assertEqual(
            get_int_from_digits([1, 0, 1, 1, 1, 0, 0], 2),
            0b1011100)

    def test_is_palidromic(self):
        self.assertTrue(is_palindromic(1234321, 10))
        self.assertTrue(is_palindromic(123321, 10))
        self.assertTrue(is_palindromic(0b101101101, 2))
        self.assertTrue(is_palindromic(0b10111101, 2))


if __name__ == '__main__':
    unittest.main()
