import unittest
import problem as p

class TestProblem(unittest.TestCase):
    def test_is_pythagorean(self):
        self.assertEquals(p.isPythagorean(3, 4, 12), True)

    def test_find_pythagorean(self):
        self.assertEquals(p.findPythagorean(12), 60)
        self.assertEquals(p.findPythagorean(1000), 31875000)

unittest.main()