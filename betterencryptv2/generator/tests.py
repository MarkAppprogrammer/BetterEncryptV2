from django.test import TestCase

from .passwordgen import passwordAlgorithm
from .transformer import parse_result


class PasswordGenTests(TestCase):
    def test_password_algorithm_returns_non_empty_string(self):
        password = passwordAlgorithm(7, 3, "personal email account")
        self.assertIsInstance(password, str)
        self.assertGreater(len(password), 0)

    def test_parse_result_extracts_two_numbers(self):
        self.assertEqual(parse_result("07 10"), ["07", "10"])
        self.assertEqual(parse_result("security=3 memorability=9"), ["3", "9"])
