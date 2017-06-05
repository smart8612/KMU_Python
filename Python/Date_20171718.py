# Input (Now_Year / Now_Month / Now_Day)

Now_Year = int(input("What year is it today? "))
Now_Month = int(input("What Month is it today? "))
Now_Day = int(input("What day is it today? "))

# Variable initialize

Days_From_Year = 0
Days_From_Month = 0
Days_From_Day = 0

# Identify Yoon Year and Add Year

for i in range(1, Now_Year) :
    Is_Yoon_Year = False

    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) :
        Days_From_Year += 366

    else : Days_From_Year += 365

# Identify Yoon Year Function

def is_yoon_year(Now_Year):
    if (Now_Year % 4 == 0 and Now_Year % 100 != 0) or (Now_Year % 400 == 0) :
        return True
    return False

month_day = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1, Now_Month) :
    Days_From_Month += month_day[i-1]
    if i == 2 and is_yoon_year(Now_Year):
        Days_From_Month += 1

Days_From_Day = Now_Day - 1

Total_Day = Days_From_Year + Days_From_Month + Days_From_Day

Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mod_day = Total_Day % 

print("Today is ", Now_Year, ".", Now_Month, ".", Now_Day, " .", Day[mod_day])
