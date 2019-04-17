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


def getPrimeFactors(number):
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


def calculateValues(maxa, maxb):
    tableOfNumbers = {}
    for a in range(2, maxa+1):
        factors = getPrimeFactors(a)
        for b in range(2, maxb+1):
            values = []
            for i in range(1, b+1):
                values = values + factors
            values.sort()
            strNumber = ''.join(map(str, values))
            if strNumber not in tableOfNumbers:
                tableOfNumbers[strNumber] = strNumber
    return len(tableOfNumbers.keys())


calculateValues(100, 100)
