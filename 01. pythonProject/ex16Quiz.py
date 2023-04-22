import random as rnd
print(rnd.random())
# import 모듈명 as 별칭
'''
컴퓨터가 1~100사이의 임의의 정수를 발생시키면
이것을 맞추는 게임을 작성하세요
이때 힌트를 주세요 ex)"더 큰 수 입니다"..
게임시도 횟수: 5번까지만 가능
5번이 넘어가면 Fail
'''
r = rnd.randint(1, 100)

answer = int(input('숫자를 맞춰보세요! (남은기회 : 5번)'))

for i in reversed(range(1, 5)):
    if(answer < r):
        answer = int(input(f'더 큰수를 입력하세요! (남은기회 : {i}번)'))
    elif(answer > r):
        answer = int(input(f'더 작은 수를 입력하세요! (남은기회 : {i}번)'))
    elif(answer == r):
        print('정답입니다!')
        break
    if (i == 1):
        print(f'실패입니다.... 정답은 {r} 이였습니다')