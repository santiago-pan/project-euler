import math


def get_number_of_digits_in_number(number):
    return max(math.floor(math.log10(abs(number))), 0) + 1


def solution():
    stop = False
    N_1 = 1
    N_2 = 1
    index = 3
    while stop is False:
        N = N_1 + N_2
        if get_number_of_digits_in_number(N) >= 1000:
            stop = True
        else:
            N_2 = N_1
            N_1 = N
            index += 1

    return index


print(solution())
