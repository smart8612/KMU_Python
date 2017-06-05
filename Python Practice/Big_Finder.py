l = [1, 4, 2, 5, 6, 3, 7]

big = l[0]

for i in range(len(l)):
    if (l[i] > big):
        big = l[i]

print(big)
