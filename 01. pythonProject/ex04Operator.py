'''
연산자(Operator)
'''
print('1. 산술 연산자: +,-,*,/,//,%, **(거듭제곱)')

x=3
y=10
print(x+y, y-x, x*y, y/x, y//x)
print(y%3) #나머지값
print(y**x) #y의 x승

#연산할 때는 연산자 우선순위를 고려해야 한다
a,b,c = 2,3,4
print(a+b-c, a+b*c, a*b/c) #1 14 1.5

print((a+b)*c) # 소괄호를 이용하여 연산자 우선순위를 바꿀 수 있다.
'''
연산시 자동 형변환
정수 < 실수 
int + int => int
int + float => float  큰 자료유형으로 자동 형변환이 일어남(promotion, upcasting)
float + float => float

#반대 방향으로 변환해야 할때는 강제형변환을 해야한다 (casting, downcasting)
'''
p=3.141592
z=p+10  # float+int=>float
print(z, type(z))

y=int(z) #강제형변환. 데이터 손실이 발생할 수 있다
print('y=',y)

m, n = 8,2
print("m={0}, n={1}".format(m, n))
'''
m과 n의 값을 치환해보자
'''
tmp=0

tmp = m
m = n
n= tmp
print("m={0}, n={1}".format(m, n))
#다중 치환
m, n = n, m
print("m={0}, n={1}".format(m, n))

print('2. 비교 연산자 -----')
'''
= : 대입 연산자
==: 비교 연산자  값이 같은지 여부를 체크. 같으면 True, 다르면 False
!= :  값이 다른지 여부를 체크. 다르면 True, 같으면 False
> : 큰가? 
>= : 크거나 같은가?
< : 작은가?
<= : 작거나 같은가 
'''
a=6
b=6.0
print('a=%d, b=%f' %(a,b))
print('a==b', a==b)
print('a!=b', a!=b)
print('a>b', a>b)
print('a>=b', a>=b)

print('3. 논리 연산자 -------')
'''
and, or, not 연산자
[1] and : 피연산자가 모두 True일때만 True
[2] or  : 피연산자 둥 1개라도 True면 True
[3] not : 논리부정연산자 True=> False, False=>True
'''
print('---and---------')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('---or---------')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#논리형
b=True
c = b
d = not b

print('c=',c, 'd=',d)

# 논리형 => 정수  True (1), False (0)
print('True를 정수로: ', int(b))
print('False를 정수로: ', int(d))



x=(5>3)
y=(5==3)
'''
x, y값 각각 출력하고
x and y
x or y
not x 
'''
print('x: {0}, y:{1}'.format(x,y))
print(x and y, x or y, not x)

age=13

print(10<=age <=20)  # True
print(age>=10 * age <=20) # False
print((age>=10) * (age<=20)) #1
print(bool((age>=10) * (age<=20))) # True

# [문제1]
# 2자리 양수를 거꾸로 뒤집어 보세요.
# 71  -->  17
'''
7*10 + 1
1*10 + 7
'''
num=input('2자리 양수를 입력하세요: ')
print('num=%s' %num)
num =int(num)
d1= num//10
d2= num%10
# print(d1, d2)
print(d2*10+d1)
# [문제2]
# 3자리 양수를 거꾸로 뒤집어 보세요.
# 123   ==> 321
num=int(input('3자리 양수 입력: '))
d1=num//100
d2=num//10 %10
d3=num%10
print(d1, d2, d3)
print(d3*100+d2*10+d1)
# [문제3]
# 4자리 양수를 거꾸로 뒤집어 보세요.
# 1234 ==> 4321

num=int(input('4자리 양수 입력: '))
d1=num//1000
d2=num//100 %10
d3=num%100//10
d4=num%10
print(d1, d2, d3, d4)
print(d4*1000+d3*100+d2*10+d1)