import math

num = int(input("Write Number! "))

for i in range(2, int(math.sqrt(num)+1)):
    if (num % i == 0):
        print("This is not prime number!")
    else :
        print("This is prime number!")
