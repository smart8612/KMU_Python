l = [1, 4, 2, 5, 6, 3, 7]

small = l[0]

for i in range(len(l)):
    if (l[i] < small):
        small = l[i]

print(small)
