def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


Year = int(input("Write Year: "))
Month = int(input("Write Month: "))
Day = int(input("Write Day: "))

Days_From_Year = 0

for i in range(1, Year):
    if isLeapYear(i):
        Days_From_Year += 366
    else:
        Days_From_Year += 365

Days_From_Month = 0
Days_At_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if isLeapYear(Year):
    Days_At_Month[1] = 29

for i in range(1, Month):
    Days_From_Month += Days_At_Month[i - 1]

Days_From_Day = Day - 1

Total_Days = Days_From_Year + Days_From_Month + Days_From_Day
Day_At_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

C = Day_At_Week[Total_Days % 7]

print(Year, ".", Month, ".", Day, ".", C)
