print('while loop문------')
'''
반복문: loop문
[1] while
[2] for
----------------
[1] while
    변수 초기화식
    while 조건식:
        실행문
        변수증감식
    - 조건 체크를 해서 조건이 True이면 실행문을 수행한 뒤, 또 다시 조건 체크를 한다
       조건이 True이면 계속 반복 실행한다. False일 경우는 while루프문을 벗어난다    
'''
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")

a=1
while a<=5000:
    print("Hi Python a=",a)
    # a=a+1
    a+=1
print('The End~~~~~ a=',a)

'''
while 문 이용해서 아래와 같은 정수값을 출력하세요
[1] 1 3 5 7 9       시작값      종료값   증감
                    1           9       2(+)
[2] 4 3 2 1 0       4           0       -1(-)
'''
x=1
while x <10:
    print(x, end=" ")
    x+=2
print()

y=4
while y>=0:
    print(y, end=" ")
    y-=1
print()

# 문제
# 0부터 99까지 출력해 보세요.             0      99       1(+)
# 0부터 99까지 거꾸로 출력해 보세요.       99      0       -1(-)
# 0부터 99까지 합계를 구하세요.

num=0
while num <100:
    # print(num, end=' ')
    print(f'{num:2d}', end='\t')  # \t : 탭키만큼 띄어쓰기를 한다
    num+=1
    if num %10==0:
        print()
        # print("\n", end='')

print('#'*50)

num=99
while num >-1:
    print(f'{num:2d}', end='\t')
    if num%10==0:
        print()
    num -= 1

print('*'*50)
'''
0 ~ 99까지의 합계
0+1+2+....+99
'''
num=0;
total=0;
while num <100:
    total+=num; #누적합
    print(f'{99-num:2d}', end='\t')
    num+=1
    if(num%10==0):
        print()
print('0~99까지의 총합: {}'.format(total))
'''
구구단의 단을 하나 입력받아 구구단을 출력하세요
7
7 x 1= 7
7 x 2=14
...
7 x 9=63
'''
num = int(input('숫자 입력: '))
d = 1
while(d < 10):
    print(f'{num} X {d} = {num * d}',sep = " ")
    d += 1

#[1] 1~50 까지 모든 정수 중 7의 배수만 출력
a=1
while a<=50:
    if a%7==0:
        print(a, end='\t')
    a+=1
print()

#[2] 1~100사이의 3과 7 의 공배수와 최소 공배수를 출력
'''
공배수: 3의 배수이면서 7의 배수도 되는 값
최소공배수: 공배수 중 최소값
'''
print('1~100까지 정수 중 3과 7의 공배수: ')
a=1
mn=100

while a<101:
    if a%3==0 and a%7==0:
        print(a, end=" ")
        if mn>a:
            mn=a
    a+=1
print('mn: ',mn)


a=1
lst=[] # list  3과 7의 최소 공배수만 저장할 리스트
while a<101:
    if(a%3==0 and a%7==0):
        lst.append(a) # list.append(값) => list의 맨 뒤에 값을 추가
    a+=1

print(lst)
#내장 함수 : min():최소값, max():최대값, abs():절대값, mean():평균값
print('최소공배수: ',min(lst))

#무한루프
num=0
while True:
    if num==100:
        break  #보조 제어문  break문은 가장 가까운 반복문을 이탈한다
    print('@@@@', num)
    num+=5
'''
보조 제어문
break : 해당 블럭을 벗어남
continue : 특정 조건일 때 아래 실행문을 건너뛰어서 계속 반복 수행함
'''
a=0
while a<101:
    a += 1
    if a%3==0 and a%7==0:
        continue  # 아래 실행문은 skip을 하고 계속 반복문을 수행함
    print(a, end=' ')






