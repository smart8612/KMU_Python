def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def closer(target1, target2, value):
    return target1 if abs(target1 - value) < abs(target2 - value) else target2


def closerSearch(sorted_ary, value):
    try:
        maxidx = len(sorted_ary) - 1
        minidx = 0

        while minidx <= maxidx:
            mididx = int((maxidx + minidx) / 2)

            if sorted_ary[mididx] > value:
                maxidx = mididx - 1

            elif sorted_ary[minidx] < value:
                minidx = mididx + 1

            elif sorted_ary[mididx] == value:
                return sorted_ary[mididx]

        return closer(sorted_ary[minidx], sorted_ary[maxidx], value)

    except IndexError:
        return sorted_ary[minidx - 1]


def whatDay(year, month, day):
    conwaysList = [0, 6, 11.5, 17, 23, 28, 34, 39.5, 45, 51, 56, 62, 67.5, 73, 79, 84, 90, 95.5]
    Days_At_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DoomsDay_At_Month = [3, 28, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    Day_At_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    Year = int(year)
    Month = int(month)
    Day = int(day)

    if 1900 <= Year < 2000:
        if isLeapYear(Year):
            Days_At_Month[1] = 29
            DoomsDay_At_Month[1] = 29
            DoomsDay_At_Month[0] = 4

        # Setting day at month if the year is leap Year
        
        conwaysList = list(map(lambda x: x + 1900, conwaysList))
        initYear = closerSearch(conwaysList, Year)

        if type(initYear) == int:
            doomsWeekDayIdx = 2 + (Year - initYear)

            if isLeapYear(Year):
                if initYear < Year:
                    doomsWeekDayIdx += 1
            else:
                if initYear < Year:
                    for i in range(initYear, Year):
                        if isLeapYear(i):
                            doomsWeekDayIdx += 1

                elif initYear > Year:
                    for i in range(Year, initYear):
                        if isLeapYear(i):
                            doomsWeekDayIdx -= 1

                if isLeapYear(initYear):
                    doomsWeekDayIdx -= 1

        elif type(initYear) == float:
            if int(initYear) == Year:
                doomsWeekDayIdx = 1

            elif initYear < Year:
                doomsWeekDayIdx = 3 + int(Year - initYear)

            elif initYear > Year:
                doomsWeekDayIdx = 1 + int(Year - initYear)

    # ----------------------------------------------------------

    doomsMonthDay = DoomsDay_At_Month[Month - 1]
    dayeval = Day - doomsMonthDay
    answer = (doomsWeekDayIdx + dayeval) % 7

    return answer
