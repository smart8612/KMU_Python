print("Great Common Divisor")

x = int(input("최대공약수를 구할 첫번째 수를 입력하세요! "))
y = int(input("최대공약수를 구할 두번째 수를 입력하세요! "))

l = [x, y]
l.sort()

mod_temp = l[1] % l[0]

while l[0] != 0:
    l[1] = l[0]
    l[0] = mod_temp
    print(l[1])
