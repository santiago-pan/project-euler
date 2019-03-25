def leapYear(year):
    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)


def yearMonthDays(year):
    leap = 1 if leapYear(year) else 0
    return [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def countSundaysFirst(startYear,
                      endYear):

    dayOfWeek = 2
    cnt = 0
    for year in range(startYear, endYear+1):
        monthsDays = yearMonthDays(year)
        for month in range(1, 13):
            lastDayOfThisMonth = monthsDays[month-1]
            for day in range(1, lastDayOfThisMonth+1):
                if dayOfWeek == 7 and day == 1:
                    cnt = cnt + 1
                if dayOfWeek == 7:
                    dayOfWeek = 1
                else:
                    dayOfWeek = dayOfWeek + 1

    return cnt
