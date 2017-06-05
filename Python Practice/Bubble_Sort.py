l = [1,3,2,4,3,5,4,6,5,7,6,8,7,9]

for i in range(len(l)):
    for j in range(1,len(l)):
        if (l[j-1] > l[j]):
            (l[j-1], l[j]) = (l[j], l[j-1])

print(l)
