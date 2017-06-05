k = int(input("Write Integer Number: "))
t = 1

for i in range(1, k+1):
    for j in range(1, i+1):
        print(t, end=" ")
        t += 1
    print()
print()