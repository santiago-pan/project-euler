def sumOfProperDivisors(number):
    sum = 1
    for factor in range(2, int(number**0.5) + 1):
        if (number % factor == 0):
            sum += factor
            if (factor != number/factor):
                sum += number/factor
    return sum


def solution(number):
    sum = 0
    for a in range(1, number):
        b = sumOfProperDivisors(a)
        if (sumOfProperDivisors(b) == a):
            if (a != b):
                sum += a
    return sum
