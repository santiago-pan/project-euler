def isDivisor(number, divisor):
    return number % divisor == 0


def isPrime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if isDivisor(number, divisor):
            return False
    return True


def solution():

    maxN = 0
    maxAB = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            noPrime = False
            while noPrime == False:
                candidate = n**2 + a*n + b
                if isPrime(candidate) == False:
                    noPrime = True
                else:
                    n += 1
                    if n > maxN:
                        maxN = n
                        maxAB = a*b

    return maxAB


print(solution())
