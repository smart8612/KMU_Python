print("Nested for")

for i in range(10) :
    for j in range(10) :
        print('*', end='')
    print()

print("Nested while")

i = 0

while (i < 10) :
    j = 0
    while (j < 10) :
        print('*', end='')
        j += 1
    print()
    i += 1
