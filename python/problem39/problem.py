def calculate_a(p, c):
    return (p*p - 2*p*c)/(2*p - 2*c)


def calculate_b(a, c):
    return (a*a + c*c)**0.5


def is_solution(p, c):
    a = calculate_a(p, c)
    b = calculate_b(a, c)
    if p == a + b + c:
        return True

    return False


def solution():
    maxSolutions = 0
    maxP = 0
    for half_p in range(1, 500):
        acc = 0
        for c in range(1, half_p):
            p = 2*half_p
            if is_solution(p, c):
                acc += 1

        if acc > maxSolutions:
            maxSolutions = acc
            maxP = half_p*2

    return maxP


print(solution())
