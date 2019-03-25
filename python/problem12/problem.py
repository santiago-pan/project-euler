import itertools
import operator

def isDivisor (number, divisor): 
    return number % divisor == 0

def isPrime (number):
    if number < 2: return False
    for divisor in range(2, int(number**0.5) + 1):
        if isDivisor(number, divisor):
            return False
    return True

def getNextPrimeNumber (currentPrime):
    currentPrime = currentPrime + 1  
    while isPrime(currentPrime) == False:
        currentPrime = currentPrime + 1
    return currentPrime

def getPrimeFactors (number):
    primes = []
    rest = number
    maxPrime = getNextPrimeNumber(1)       
    while rest > 1:
        if rest % maxPrime == 0:
            primes.append(maxPrime)
            rest = rest / maxPrime
        else:
            maxPrime = getNextPrimeNumber(maxPrime)

    return primes

def sumOfAllNumbers (number):
    return number * (number + 1) / 2


def getTriangleNumber(current):
    return sumOfAllNumbers(current)

def getDivisors(number):
    factors = getPrimeFactors (number)
    uniqueCombinations = set()
    for i in range(1, len(factors)):
        uniqueCombinations.update(
            set(itertools.combinations(factors, i)))
    
    combinationProduct = list(reduce(lambda x,y: x*y, i) for i in uniqueCombinations)
    combinationProduct.sort()

    return [1] + combinationProduct + [number]


def findFirstNumberWithMoreDivisorsThan(numberOfDivisors):
    number = 1
    divisors = [1,2]
    while (len(divisors) <= numberOfDivisors):
        number = number+1
        triangleNumber = getTriangleNumber(number)
        divisors = getDivisors(triangleNumber)        
    return triangleNumber