def IsLeapYear(Year):
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0) :
        return True
    else :
        return False

print("Identifying Leap Year Program!")
Year = int(input("Write Year! "))

if (IsLeapYear(Year) == True):
    print(Year, " is LeapYear!")
else :
    print(Year, " is not LeapYear!")
