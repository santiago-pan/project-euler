
from math import factorial

# Here the key is to find what is the limit until we have to search.
#
# In this case we know that:
#
# 9! = 362880
# So:
# 99 < 2 x 362880
# 999 < 3 x 362880
# ...
# 9.999.999 > 7 x 362880 =  2.540.160
#
# So, any number bigger than 9.999.999 will not be possible to express by the sum of its factorial numbers


def getDigitsFactorialSum(number):
    acc = 0
    while (number > 0):
        acc += factorial(number % 10)
        number = number / 10
    return acc


def solution():
    acc = 0
    for number in range(3, 10000000):
        candidate = getDigitsFactorialSum(number)
        if candidate == number:
            acc += candidate

    return acc


print(solution())
