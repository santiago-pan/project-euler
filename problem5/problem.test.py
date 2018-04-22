import unittest
import problem as p

class TestProblem(unittest.TestCase):
    def test_get_array_of_numbers(self):
        self.assertEquals(p.getArrayOfNumbers(5), [1,2,3,4,5])
        self.assertEquals(p.getArrayOfNumbers(10), [1,2,3,4,5,6,7,8,9,10])

    def test_primes_decomposition(self):
        self.assertEqual(p.getPrimeFactors(10), [2,5])
        self.assertEqual(p.getPrimeFactors(11), [11])
        self.assertEqual(p.getPrimeFactors(21), [3,7])
        self.assertEqual(p.getPrimeFactors(32), [2,2,2,2,2])
        self.assertEqual(p.getPrimeFactors(800), [2,2,2,2,2,5,5])

    def test_get_factors_hash(self):
        self.assertEqual(p.groupFactorsInHash([2,2]), {2:2})
        self.assertEqual(p.groupFactorsInHash([2,2,2,2,2,5,5]), {2:5,5:2})
        self.assertEqual(p.groupFactorsInHash([1,2,2,3,3,3]), {1:1,2:2,3:3})

    def test_get_max_factors(self):
        
        self.assertEqual(p.getMaxFactors([
            {2:2,3:3},            
            {2:3,3:2}
        ]),{2:3,3:3})
        
        self.assertEqual(p.getMaxFactors([
            {2:2,3:3,7:1},            
            {2:3,3:2,11:1}
        ]),{2:3,3:3,7:1,11:1})

        self.assertEqual(p.getMaxFactors([
            {2:3},
            {3:2},
            {5:1},
            {7:1}
        ]),{2:3,3:2,5:1,7:1})

    def test_product_of_factors(self):
        self.assertEqual(p.productOfFactors({2:3, 3:3, 7:1, 11:1}), 16632)
        self.assertEqual(p.productOfFactors({2:3,3:2,5:1,7:1}), 2520)

    def test_solution_of_problem(self):
        self.assertEqual(p.solution(10),2520)
        self.assertEqual(p.solution(20),232792560)
        self.assertEqual(p.solution(200),337293588832926264639465766794841407432394382785157234228847021917234018060677390066992000L)

unittest.main()