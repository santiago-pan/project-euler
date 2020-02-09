import time


def isDivisor(number, divisor):
    return number % divisor == 0


def isPrime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if isDivisor(number, divisor):
            return False
    return True


def checkTruncatableNumber(number):
    numDigits = len(str(number))
    for index in range(1, numDigits+1):

        # Right check, starting with lower number
        rDivisor = 10**index
        rPrime = number % (rDivisor)
        if rPrime not in primes and isPrime(rPrime) is False:
            return False
        else:
            primes[rPrime] = True

        # Left check, starting with lower number
        lDivisor = 10**(numDigits - (index))
        lPrime = int(number/(lDivisor))
        if lPrime not in primes and isPrime(lPrime) is False:
            return False
        else:
            primes[lPrime] = True
    return True


# Keep trak of found prime numbers
primes = {}


def solution():
    numFound = 0
    number = 11
    sum = 0
    while (numFound < 11):
        isTruncatable = checkTruncatableNumber(number)
        if isTruncatable is True:
            numFound += 1
            sum += number
        number += 1
    return sum


start = time.time()
print(solution())
end = time.time()
print(end - start)
print(primes)
