# Input (Now_Year / Now_Month / Now_Day) and Output

Now_Year = int(input("What year is it today? "))
Now_Month = int(input("What Month is it today? "))
Now_Day = int(input("What day is it today? "))

print("Today is ", Now_Year, ".", Now_Month, ".", Now_Day, ".")

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

# Identify Now_Year is Yoon Year

if (Now_Year % 4 == 0 and Now_Year % 100 != 0) or (Now_Year % 400 == 0) :
    Is_Yoon_Year = True

# Identify Month and Add days

for i in range(1, Now_Month) :
    if (i == 1) : Days_From_Month += 31
    if (i == 2 and Is_Yoon_Year == False) : Days_From_Month += 28
    elif (i == 2 and Is_Yoon_Year == True)  : Days_From_Month += 29
    if (i == 3) : Days_From_Month += 31
    if (i == 4) : Days_From_Month += 30
    if (i == 5) : Days_From_Month += 31
    if (i == 6) : Days_From_Month += 30
    if (i == 7) : Days_From_Month += 31
    if (i == 8) : Days_From_Month += 31
    if (i == 9) : Days_From_Month += 30
    if (i == 10) : Days_From_Month += 31
    if (i == 11) : Days_From_Month += 30
    if (i == 12) : Days_From_Month += 31

# Sum Total day

Days_From_Day = Now_Day - 1

Total_Day = Days_From_Year + Days_From_Month + Days_From_Day

# Modulus Total_Day

if (Total_Day % 7) == 0 :
    print("Monday")
if (Total_Day % 7) == 1 :
    print("Tuesday")
if (Total_Day % 7) == 2 :
    print("Wednesday")
if (Total_Day % 7) == 3 :
    print("Thursday")
if (Total_Day % 7) == 4 :
    print("Friday")
if (Total_Day % 7) == 5 :
    print("Saturday")
if (Total_Day % 7) == 6 :
    print("Sunday")
