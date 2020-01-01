from math import floor, ceil


def isPalindrome(number):
    if number == number[::-1]:
        return True
    return False


def solution():
    acc = 0
    for i in range(0, 1000000):
        if (isPalindrome(str(i)) and isPalindrome(bin(i)[2:])):
            acc += i

    return acc


print(solution())
