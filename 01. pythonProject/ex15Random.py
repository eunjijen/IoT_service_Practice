print('#random 모듈 활용')
import random
'''
random(): 0.0<= r <1.0
    임의의 실수값을 발생시켜 반환하는 함수
'''
r=random.random()
print('r=',r)
# help(random.random)
'''
[1] 0<= r2 <10 임의의 정수값을 발생시켜 출력해보기
random.random()활용하기

[2] 5<= r3 <15
'''
r2=int(random.random()*10)
print('r2=',r2)

r3=int(random.random()*10)+5
print('r3=',r3)
'''
random.random()*범위 + 시작수

43<= r4 <66
'''
r4=int(random.random()*23 + 43)
print('r4=',r4)
'''
- randint(a,b) : a<= N <=b :a,b사이의 랜덤한 정수를 반환한다
- randrange(a,b): a<= N <b :a,b사이의 랜덤한 정수를 반환한다 (b를 포함하지 않음)
- choice(seq) : sequnece에서 임의의 요소를 선택해서 반환한다.
'''
print('-'*30)
'''
77<= r5 <=99
'''
r5=random.randint(77,99)
print('r5=',r5)

print(random.randrange(100,200))

names=['홍길동','김철수','최영희','이순신']
luckyman=random.choice(names)
print(luckyman)







