import random

Lotto_Number = set()

#집합을 이용하여 중복된 수를 처리합니다.
#Lotto_Number 집합의 element가 5개가 될때까지 (1,45) 범위의 수를 임의 추출하여 추가하고 Lotto_Number을 출력합니다

while len(Lotto_Number) < 5 :

    Lotto_Number.add(random.randint(1,45))

print(Lotto_Number)

#Sample 메소드를 이용해서도 프로그램을 작성할 수 있습니다!

print(random.sample(range(1,46),5))

#두 방법의 본질적인 차이를 생각해 보았을 때,
#중복을 고려하지 않는 집합의 성질을 이용하는가, 아니면 상자에 담긴 숫자를 비복원 추출을 하는가가 차이 인 것 같습니다!
