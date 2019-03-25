import unittest
import problem as p


class TestProblem(unittest.TestCase):

    def test_sum_of_proper_divisors(self):
        self.assertEqual(p.getCycle(6), 2)
        self.assertEqual(p.getCycle(5), 1)
        self.assertEqual(p.getCycle(61), 61)
        self.assertEqual(p.getCycle(67), 34)

    def test_solution(self):
        self.assertEqual(p.solution(1000), 983)        

unittest.main()
