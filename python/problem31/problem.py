import time


def solution():
    total = 1  # Since 2f is the first option
    for a in range(0, 3):
        for b in range(0, 1+(200-100*a)/50):
            for c in range(0, 1+(200-100*a-50*b)/20):
                for d in range(0, 1+(200-100*a-50*b-20*c)/10):
                    for e in range(0, (1+(200-100*a-50*b-20*c-10*d)/5)):
                        for f in range(0, (1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
                            total += 1

    return total


start = time.time()
print(solution())
end = time.time()
print(end - start)