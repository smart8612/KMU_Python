Year = int(input("Write year to know Yoon year or not "))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0) :
    print(Year, " is Yoon year!")
else :
    print(Year, " is not Yoon year!")
