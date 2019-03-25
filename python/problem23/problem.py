import time

LIMIT = 28123


def sumOfProperDivisors(number):
    sum = 1
    for factor in range(2, int(number**0.5) + 1):
        if (number % factor == 0):
            sum += factor
            if (factor != number/factor):
                sum += number/factor
    return sum


def isAbundantNumber(number):
    return sumOfProperDivisors(number) > number


def getAllAbundantNumbersUntil(number):
    abuntandNumbers = []
    for n in range(12, number+1):
        if isAbundantNumber(n):
            abuntandNumbers.append(n)
    return abuntandNumbers


def getAllSumsOfAbundantNumberSum(abundantNumbers, number):
    validNumbers = [False for x in range(LIMIT+1)]
    allSums = 0
    for n in abundantNumbers:
        for m in abundantNumbers:
            currentSum = n+m
            if currentSum <= LIMIT:
                if validNumbers[currentSum] is False:
                    validNumbers[currentSum] = True
                    allSums += currentSum
            else:
                break

    return allSums


def simpleNumbersSum(number):
    sum = 0
    for n in range(1, number+1):
        sum += n
    return sum


def solution():
    abundantNumbers = getAllAbundantNumbersUntil(LIMIT)
    allAbumdantNumbersSum = getAllSumsOfAbundantNumberSum(
        abundantNumbers, LIMIT)
    allNumbersSum = simpleNumbersSum(LIMIT)
    return allNumbersSum - allAbumdantNumbersSum


t = time.time()
solution()
elapsed = time.time() - t
print(elapsed)
