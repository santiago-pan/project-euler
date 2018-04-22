import unittest
import problem as p
import time

class TestProblem(unittest.TestCase):
    def test_is_divisor(self):
        self.assertTrue(p.isDivisor(2,2))
        self.assertTrue(p.isDivisor(4,2))
        self.assertTrue(p.isDivisor(6,2))
        self.assertFalse(p.isDivisor(5,2))

    def test_is_prime(self):
        self.assertTrue(p.isPrime(2))
        self.assertTrue(p.isPrime(3))
        self.assertTrue(p.isPrime(5))
        self.assertTrue(p.isPrime(7))
        self.assertFalse(p.isPrime(9))

    def test_get_next_prime(self):
        self.assertEquals(p.getNextPrimeNumber(2), 3)
        self.assertEquals(p.getNextPrimeNumber(3), 5)
        self.assertEquals(p.getNextPrimeNumber(5), 7)

    def test_get_primes_factor(self):
        self.assertEqual(p.getPrimeMaxFactor(600851475143), 6857)

unittest.main()