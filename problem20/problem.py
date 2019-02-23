def sumAllNumberDigits(number, acc=0):
    if number > 0:
        return acc + sumAllNumberDigits(number / 10, number % 10)
    else:
        return acc


def factorial(number, acc=1):
    if (number == 1):
        return acc
    else:
        return factorial(number - 1, acc * number)
