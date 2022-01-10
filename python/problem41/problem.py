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


def isPandigital(n):
    n = str(n)
    s = len(n)
    return len(n) == s and not '1234567890'[:s].strip(n)


def solution():
    n = 7654321

    stop = False
    while (stop is False):
        if isPandigital(n) is True:
            if isPrime(n) is True:
                print(n)
                stop = True
        n -= 2
    return n


solution()
