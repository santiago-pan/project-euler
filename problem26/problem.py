def getCycle(divisor):
    rem = 1
    stop = False
    reminders = []
    currentDecimal = 0
    while stop is False:
        currentDecimal += 1
        rem = rem*10 % divisor
        # Check if reminder is in the list
        for idx, r in enumerate(reminders):
            if rem == r:
                stop = True
                return currentDecimal - idx

        # Check if reminder is zero
        if rem == 0:
            stop = True
            return currentDecimal

        reminders.append(rem)


def solution(max):
    d = 0
    for i in range(2, max+1):
        current = getCycle(i)
        if current > d:
            d = current

    return d


print(solution(1000))
