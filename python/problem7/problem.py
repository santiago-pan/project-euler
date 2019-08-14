import sys


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
    while isPrime(currentPrime) == False:
        currentPrime = currentPrime + 1
    return currentPrime


# Recursion in python can cause maximum recursion depth
sys.setrecursionlimit(15000)


def getPrimeAtPositionRecursive(toPosition, position=0, prime=1):
    if (position == toPosition):
        return prime
    else:
        prime = getNextPrimeNumber(prime)
        return getPrimeAtPositionRecursive(toPosition, position + 1, prime)


def getPrimeAtPosition(toPosition):
    position = 0
    prime = 1
    while (position < toPosition):
        prime = getNextPrimeNumber(prime)
        position = position + 1
    return prime
