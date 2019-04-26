# For N*(9**5), N=6 is the first value for N that returns a number with less digits than N
# So 6*(9**5) is a good upper limit


def solution():
    MAX = 6*(9**5)
    total = 0
    for candidate in range(2, MAX):
        digitsSum = 0
        for digit in str(candidate):
            digitsSum += int(digit) ** 5

        if digitsSum == candidate:
            total += candidate

    return total


print("solution", solution())
