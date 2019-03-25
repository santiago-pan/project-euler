import unittest
from problem import twoPowToNumber
from problem import sumAllNumberDigits
from problem import problemSolution

class TestProblem(unittest.TestCase):
    
    def test_two_to_power(self):
        self.assertEqual(twoPowToNumber(6), 64)

    def test_sum_all_numbers_from_digit(self):
        self.assertEqual(sumAllNumberDigits(12345), 15)
        self.assertEqual(sumAllNumberDigits(32768), 26)

    def test_problem_solution(self):
        self.assertEqual(problemSolution(), 1366)
unittest.main()