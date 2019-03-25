import unittest
import problem as p


class TestProblem(unittest.TestCase):

    def test_sum_of_proper_divisors(self):
        self.assertEqual(p.sumOfProperDivisors(220), 284)
        self.assertEqual(p.sumOfProperDivisors(284), 220)

    def test_is_abundant_number(self):
        self.assertEqual(p.isAbundantNumber(18), True)
        self.assertEqual(p.isAbundantNumber(12), True)
        self.assertEqual(p.isAbundantNumber(19), False)
        self.assertEqual(p.isAbundantNumber(11), False)

    def test_get_all_abuntant_numbers(self):
        self.assertEqual(p.getAllAbundantNumbersUntil(41),
                         [12, 18, 20, 24, 30, 36, 40])

    def test_get_all_abundant_numbers_sum(self):
        self.assertEqual(p.getAllSumsOfAbundantNumberSum(
            [12, 18, 20, 24, 30, 36, 40], 41), 1092)

    def test_solution(self):
        self.assertEqual(p.solution(), 4179871)



unittest.main()
