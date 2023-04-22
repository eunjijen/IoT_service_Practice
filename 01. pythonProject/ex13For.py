print('for loop문---------')
'''
for 변수 in 리스트:  #열거형객체
    실행문
    
for 변수 in 문자열:
    실행문    
    
for 변수 in range(start, stop, step):
    실행문    
'''
lst=[10,20,30,40]
total=0
for val in lst:
    print(val)
    total+=val
print('lst의 총합계: ',total)
print('sum(lst): ', sum(lst))

'''
lst에 저장된 값들의 거듭제곱값을 출력하세요
'''
for val in lst:
    print(val**2, end=' ')
print()

for ch in "Hello Python~~":
    print(ch)
print('-'*50)

nums=range(10)  # range(10) : 0 ~ 9
print(nums, type(nums))
# help(range)

for k in nums:
    print(k,end=" ")

# range(stop): 0~ (stop-1)
print()
# 5부터 99까지 반복문 돌면서 홀수값들만 출력하세요
# for 변수 in range(시작값, 종료값, 증가치):
for k in range(5,100,2):
    print(k, end=' ')
print()
# [문제1] range() 이용해서
# 0~9 사이의 숫자를 거꾸로 출력해 보세요. (for문)
for i in range(10):
    print(9-i, end=' ')
print()

for i in range(9,-1,-1): #감소식
    print(i, end=' ')
print()

# reversed(range()) : 역으로 감소하면서 진행한다
for i in reversed(range(10)):
    print(i, end=' ')
print()

'''
for 변수 in range():
    실행문1
else:
    실행문2
'''
for i in range(5):
    print('@',end=' ')
else:
    print('반복문이 종료되었어요!!')

'''    
# [문제2]
# 0~100 사이의 숫자를 출력하되 5단위의
# 숫자 부분에 "땅콩" 출력, 10단위의 숫자 부분에는 "찐콩", 나머지는 "숫자"를
# 출력하세요. (for문)
1, 2, 3, 4 땅콩, 6 ,7, 8, 9,찐콩,11,12,13,14, 땅콩...
'''
for i in range(1, 101):
    if(i%10 == 0):
        print("찐콩", end = " ")
    elif(i%5 == 0):
        print("땅콩", end = " ")
    else:
        print(i, end = " ");
'''
# [문제3]
#1+2+3+....+10=55
#1~10까지의 합을 구하되 덧셈식도 함께 출력하기

삼항 조건 연산자를 이용해서 축약해보세요
변수 = 참일때값 if 조건 else 거짓일때값
'''
print()
total=0
for i in range(1,11):
    if i<10:
        print(i,end="+")
    else:
        print(i,end="=")
    total+=i
print(total)

total = 0
for i in range(1, 11) :
    #print(i, end="+") if i < 10 else print(i, end="=")
    sign="+" if i<10 else "="
    print(i, end=sign)
    total += i
print(total)