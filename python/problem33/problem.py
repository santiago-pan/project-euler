def getCombinations(numerator, denominator, digit):

    n = numerator
    d = denominator
    D = digit
    f1 = (n*10 + D) / (d*10 + D)
    f2 = (n*10 + D) / (D*10 + d)
    f3 = (D*10 + n) / (d*10 + D)
    f4 = (D*10 + n) / (D*10 + d)

    if f1 == n/d:
        print("%d/%d" % (n, d))
        print("%d/%d\n" % ((n*10 + D), (d*10 + D)))
    if f2 == n/d:
        print("%d/%d" % (n, d))
        print("%d/%d\n" % ((n*10 + D), (D*10 + d)))
    if f3 == n/d:
        print("%d/%d" % (n, d))
        print("%d/%d\n" % ((D*10 + n), (d*10 + D)))
    if f4 == n/d:
        print("%d/%d" % (n, d))
        print("%d/%d\n" % ((D*10 + n), (D*10 + d)))


def solution():
    for denominator in range(1, 10):
        for numerator in range(1, denominator):
            for digit in range(1, 10):
                getCombinations(float(numerator), float(denominator), digit)


solution()
