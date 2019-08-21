from math import log10
from math import floor
import time


def getAllPrimeNumbers(stopNumber):
    primes = [1]*stopNumber
    primes[0] = 0
    primes[1] = 0
    for divisor in range(2, int(stopNumber**0.5) + 1):
        if primes[divisor] == 0:
            continue
        for number in range(divisor*divisor, stopNumber, divisor):
            primes[number] = 0

    primesObject = {}
    for candidate in range(2, stopNumber):
        if primes[candidate] == 1:
            primesObject[candidate] = numDigits(candidate)

    return primesObject


def numDigits(number):
    return int(floor(log10(number))+1)


def allRotationsArePrime(number, nDigits, primes):
    for n in range(0, nDigits):
        if number in primes:
            number = rotateNumber(number, nDigits)
            continue
        return False
    return True


def rotateNumber(number, nDigits):
    return int(number/10+number % 10*10**(nDigits-1))


def solution():
    acc = 0
    primes = getAllPrimeNumbers(1000000)

    for prime in primes.keys():
        nDigits = primes[prime]
        allPrimes = allRotationsArePrime(prime, nDigits, primes)
        if allPrimes is True:
            acc += 1
    return acc


start = time.time()
print(solution())
end = time.time()
print(end - start)
