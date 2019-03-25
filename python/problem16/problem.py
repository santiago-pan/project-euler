# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

def twoPowToNumber (number):
    return 2 ** number

def sumAllNumberDigits (number, acc = 0):
    if number > 0:
        return acc + sumAllNumberDigits(number / 10, number % 10)
    else:
        return acc

def problemSolution ():
    number = twoPowToNumber(1000)
    return sumAllNumberDigits(number)