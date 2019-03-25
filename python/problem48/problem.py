def solution():
    acc = 0
    for i in range(1, 1001):
        acc += i**i

    numberStr = str(acc)

    return numberStr[len(numberStr)-10:len(numberStr)]


print(solution())