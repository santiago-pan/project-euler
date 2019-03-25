import unittest
import problem as p

class TestProblem(unittest.TestCase):
    
    def test_primes_decomposition(self):
        self.assertEqual(p.getPrimeFactors(10), [2,5])
        self.assertEqual(p.getPrimeFactors(11), [11])
        self.assertEqual(p.getPrimeFactors(21), [3,7])
        self.assertEqual(p.getPrimeFactors(32), [2,2,2,2,2])
        self.assertEqual(p.getPrimeFactors(800), [2,2,2,2,2,5,5])

    def test_sum_of_all_numbers(self):
        self.assertEqual(p.sumOfAllNumbers(10), 55)
    def test_get_triangle_number(self):
        self.assertEqual(p.getTriangleNumber(1), 1)
        self.assertEqual(p.getTriangleNumber(2), 3)
        self.assertEqual(p.getTriangleNumber(3), 6)
        self.assertEqual(p.getTriangleNumber(4), 10)
        self.assertEqual(p.getTriangleNumber(5), 15)
        self.assertEqual(p.getTriangleNumber(6), 21)
        self.assertEqual(p.getTriangleNumber(7), 28)

    def test_get_all_divisors_by_factors(self):
        self.assertEqual(p.getDivisors(24),[1,2,3,4,6,8,12,24])
        self.assertEqual(p.getDivisors(28),[1,2,4,7,14,28])
        self.assertEqual(p.getDivisors(66),[1, 2, 3, 6, 11, 22, 33, 66])

    def test_get_number_for_problem(self):
        self.assertEqual(p.findFirstNumberWithMoreDivisorsThan(5), 28)
        self.assertEqual(p.findFirstNumberWithMoreDivisorsThan(500), 66)

unittest.main()