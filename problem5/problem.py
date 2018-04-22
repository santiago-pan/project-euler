from functools import reduce
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def getArrayOfNumbers (toNumber):
    return [i for i in range(1,toNumber + 1)]

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

def updateHash (acc, current):
    if current in acc.keys():
        acc[current] = acc[current]+1
    else:
        acc[current] = 1
    return acc

def groupFactorsInHash (factors):
    return reduce(updateHash, factors, {})


def getMcmFactors (acc, current):    
    for key in current.keys():
        if key in acc.keys():
            if current[key] > acc[key]:
                acc[key] = current[key]                
        else:
            acc[key] = current[key]
    return acc

def getMaxFactors(factorsList):
    return reduce(getMcmFactors, factorsList, {})

def multiplyFactors(acc, val):    
    acc = acc * pow(val[0],val[1])
    return acc

def productOfFactors(factors):    
    return reduce(multiplyFactors, factors.items(), 1)

def solution(toNumber):
    numbers = getArrayOfNumbers(toNumber)
    allFactors = []
    for number in numbers:
        primes = getPrimeFactors(number)
        factors = groupFactorsInHash(primes)
        hashFactors = groupFactorsInHash(factors)
        allFactors.append(factors)

    maxFactors = getMaxFactors(allFactors)

    return productOfFactors(maxFactors)