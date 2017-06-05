# Function
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

# Main Structure

print("Greatest common divisor")

x = int(input("최대공약수를 구할 첫번째 수를 입력하세요! "))
y = int(input("최대공약수를 구할 두번째 수를 입력하세요! "))

print(gcd(x, y))
