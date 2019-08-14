import unittest
import problem as p


class TestProblem(unittest.TestCase):
    def test_get_prime_at_position(self):
        self.assertEquals(p.getPrimeAtPositionRecursive(6), 13)
        self.assertEquals(p.getPrimeAtPositionRecursive(10001), 104743)
        self.assertEquals(p.getPrimeAtPosition(6), 13)
        self.assertEquals(p.getPrimeAtPosition(10001), 104743)


unittest.main()
