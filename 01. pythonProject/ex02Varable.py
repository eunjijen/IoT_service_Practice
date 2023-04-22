a=8
# a: 변수(variable, field, property)
'''
변수
- 데이터를 일시적으로 보관하거나, 처리 결과를 담을 수 있는 기억장소
 a-------->{메모리주소값:8}
- 파이썬의 경우 값이 객체(Object) 형태로 메모리에 저장되고
   이 곳을 변수가 참조한다
'''
print(f'변수 a의 값은 {a}')
print(f'변수 a의 주소값: {id(a)}')

'''
반지름이 5인 원의 면적 : pi*r*r
            원의 둘레 : 2*pi*r
'''
print(3.14*5*5,  2*3.14*5)

r=5
pi=3.141592
print(f'반지름이 {r}인 원의 면적:{pi*r*r}')
print(f'반지름이 {r}인 원의 둘레:{2*pi*r}')

r=90
print(r, type(r)) #90 <class 'int'>  정수형
r=5.78
print(r, type(r)) #5.78 <class 'float'> 실수형

r="3.14"
print(r, type(r)) #3.14 <class 'str'> 문자열
"""
#1, 파이썬의 자료형(Data Type)
[1] 숫자 타입 (Numeric): 정수 int (크기 : 무제한),  실수 float 
[2] 불린 타입 (Logical): 참,거짓 bool (True, False)
[3] 문자열 타입(Character): 문자, 문자열 str (크기: 무제한)
"""
'''
변수값을 출력하고 옆에 자료형도 출력해보세요
-변수명
  영문자로 시작, 숫자도 섞어쓸 수 있다. 주의] 숫자로 시작해선 안된다
  특수문자를 사용해선 안된다
  키워드(예약어)를 변수로 사용하면 안된다
'''
b1=100
b2=200
# 3c=300 [x]
#c3@!=300 [x]
c3_=300
# if =400 [x]
# print(if)

import keyword
'''예약어 목록 확인'''
print('-'*50)
print(keyword.kwlist)
print('-'*50)

intVar=123
floatVar=-8.12
strVar='Python'
strVar2="""
이것도 문자열
입니다
"""
boolVar1=True
boolVar2=False
print(intVar, type(intVar))
print(floatVar, type(floatVar))
print(strVar, type(strVar))
print(strVar2, type(strVar2))
print(boolVar1, type(boolVar1))

x=3.14
y=314e-2  # 314 * 10^-2
z=314E+10 #314 * 10^10
'''
e, E : 과학적 표기법(지수)
'''
print(x, type(x))
print(y, type(y))
print(z, type(z))

st='Hello'
print(st)
print(str(x))

#bool형 : 비교/조건 표현식의 결과를 참/거짓으로 저장
b=True
c=(100==100.1)
print(b, type(b))
print(c, type(c))
'''
멀티라인
주석
'''
strVar='''
멀티라인
문자열
'''
strVar2="멀티라인\n문자열"
print(strVar2)

print(strVar)

# Q1 자신의 이름,몸무게,나이를
# 변수로 선언하고 값을 대입한 후
# 결과를 출력하세요
name="홍길동"
weight=55
age=22
print(f'''
이  름: {name}
몸무게: {weight} kg
나  이: {age} 세
''')

# 변수에 값을 대입하는 것을 값을 할당한다
x=9
y=7
print(x, y)
x, y =900, 700
print(x, y)

a=b=c=d=200
print(a, b, c, d)

e=123.12
f="111.11"

'''
e+f값을 출력해봅시다
'''
print(str(e)+f) #문자열 결합
print(e+float(f)) # 덧셈
#문자열 => 실수로 변환  float()
#문자열 => 정수로 변환  int()
