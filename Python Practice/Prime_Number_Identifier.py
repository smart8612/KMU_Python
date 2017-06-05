import math

num = int(input("Write Number! "))
l = list(range(2, num+1))

for i in l[1:]:
    if (l[i] % 2 == 0):
        l.remove(i)

print(l)
