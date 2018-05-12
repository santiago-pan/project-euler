import unittest
from problem import isEven
from problem import getNextNumber
from problem import generateSeries
from problem import findLongestSerie

class TestProblem(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(isEven(2), True)
        self.assertEqual(isEven(5), False)
        self.assertEqual(isEven(6), True)
        self.assertEqual(isEven(11), False)
        self.assertEqual(isEven(4), True)
        self.assertEqual(isEven(7), False)

    def test_get_next_if_even(self):
        self.assertEqual(getNextNumber(2), 1)
        self.assertEqual(getNextNumber(3), 10)

    def test_generate_series(self):
        self.assertEqual(generateSeries(13), 10)
        self.assertEqual(generateSeries(9), 20)

    def test_find_longest_serie(self):
        self.assertEqual(findLongestSerie(9), 9)
        self.assertEqual(findLongestSerie(1000000), 837799)

unittest.main()