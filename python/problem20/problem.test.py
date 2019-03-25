import unittest
from problem import factorial
from problem import sumAllNumberDigits


class TestProblem(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(10), 3628800)

    def test_sum_all_numbers_from_digit(self):
        self.assertEqual(sumAllNumberDigits(12345), 15)
        self.assertEqual(sumAllNumberDigits(32768), 26)

    def test_solution(self):
        n = factorial(100)
        self.assertEqual(sumAllNumberDigits(n), 648)


unittest.main()
