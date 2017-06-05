fibonacci_array = [1,2]

sumi = 0

for i in range(1, 4000001):

    fibonacci_array.append(fibonacci_array[i] + fibonacci_array[i+1])

for i in range(len(fibonacci_array)):

    if (fibonacci_array[i] % 2 == 0 and fibonacci_array[i] <= 4000000):

        sumi += fibonacci_array

print(sumi)
