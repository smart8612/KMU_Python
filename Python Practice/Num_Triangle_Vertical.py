k = int(input("Write Integer Number: "))

for i in range(1, k+1):
    print(i, end="")
    for j in range(1, i+1):
        print(i + (k-1-i))
    print()