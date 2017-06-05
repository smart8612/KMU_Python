# Function
def factorialResult(Num):
    fac = 1
    for i in range(1, Num+1):
        fac *= i
    return fac

# Main Structure

print("팩토리얼을 계산하여 각 자리수별 합을 계산해주는 프로그램 입니다.")
Num = int(input("숫자를 입력하세요! "))

array = list(str(factorialResult(Num)))

for i in range(len(array)):

    sumbyindex += int(array[i])

print(sumbyindex)
