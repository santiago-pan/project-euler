import numpy as np
import unittest

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def isMultiple(num):
    NUM_A = 3
    NUM_B = 5

    if (num % NUM_A == 0) or (num % NUM_B == 0):
        return True
    else:
        return False


def getAllMultiples(num):
    multiplos = []
    for i in range(1, num):
        if isMultiple(i):
            multiplos.append(i)

    return multiplos


def addNumbers(numbers):
    return sum(numbers)


def problem_1_solution():
    print(addNumbers(getAllMultiples(1000)))


problem_1_solution()

# TESTS


class TestProblem1(unittest.TestCase):
    def test_is_multiple(self):
        self.assertEqual(isMultiple(3), True)
        self.assertEqual(isMultiple(5), True)
        self.assertEqual(isMultiple(6), True)
        self.assertEqual(isMultiple(10), True)
        self.assertEqual(isMultiple(1), False)
        self.assertEqual(isMultiple(2), False)

    def test_multiplos_below(self):
        self.assertEqual(getAllMultiples(10), [3, 5, 6, 9])

    def test_add_numbers(self):
        self.assertEqual(addNumbers([3, 5, 6, 9]), 23)


unittest.main()
