import unittest
from problem import leapYear
from problem import yearMonthDays
from problem import countSundaysFirst


class TestProblem(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(leapYear(2000), True)
        self.assertEqual(leapYear(1901), False)
        self.assertEqual(leapYear(1908), True)
        self.assertEqual(leapYear(1916), True)
        self.assertEqual(leapYear(1924), True)
        self.assertEqual(leapYear(1948), True)
        self.assertEqual(leapYear(1800), False)
        self.assertEqual(leapYear(1900), False)
        self.assertEqual(leapYear(1600), True)

    def test_year_month_days(self):
        self.assertEqual(yearMonthDays(2000), [
                         31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        self.assertEqual(yearMonthDays(1901), [
                         31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    def test_count_sundays(self):
        self.assertEqual(countSundaysFirst(1901, 2000), 171)


unittest.main()
