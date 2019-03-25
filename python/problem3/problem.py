from functools import reduce
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def sum(a, b):
    return a + b


def doFilter(numbers):
    return filter(lambda x: x % 2 == 0, numbers)


def doReduce(numbers):
    return reduce(lambda acc, current: acc + current, numbers, 0)


def isDivisor(number, divisor):
    return number % divisor == 0


def isPrime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if isDivisor(number, divisor):
            return False
    return True


def getNextPrimeNumber(currentPrime):
    currentPrime = currentPrime + 1
    while isPrime(currentPrime) is False:
        currentPrime = currentPrime + 1
    return currentPrime


def getPrimeMaxFactor(number):
    rest = number
    maxPrime = getNextPrimeNumber(1)
    while rest > 1:
        if rest % maxPrime == 0:
            rest = rest / maxPrime
        else:
            maxPrime = getNextPrimeNumber(maxPrime)

    return maxPrime
