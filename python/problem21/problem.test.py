import unittest
import problem as p


class TestProblem(unittest.TestCase):

    def test_sum_of_proper_divisors(self):
        self.assertEqual(p.sumOfProperDivisors(220), 284)
        self.assertEqual(p.sumOfProperDivisors(284), 220)

    def test_solution(self):
        self.assertEqual(p.solution(10000), 31626)


unittest.main()
