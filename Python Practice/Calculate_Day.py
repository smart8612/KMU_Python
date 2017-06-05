def IsLeapYear(Year):
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        return True
    else :
        return False

Now_Year = int(input("Write Year! "))
Now_Month = int(input("Write Month! "))
Now_Day = int(input("Write Day! "))

Days_From_Year = 0

for i in range(1, Now_Year):
    if (IsLeapYear(i) == True):
        Days_From_Year += 366
    else :
        Days_From_Year += 365

Days_From_Month = 0
Days_At_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (IsLeapYear(Now_Year) == True):
    Days_At_Month[1] = 29

for i in range(1, Now_Month):
    Days_From_Month += Days_At_Month[i-1]

Days_From_Day = Now_Day - 1

Total_Days = Days_From_Year + Days_From_Month + Days_From_Day
Day_At_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

C = Day_At_Week[Total_Days % 7]

print(Now_Year, ".", Now_Month, ".", Now_Day, ".", C)
