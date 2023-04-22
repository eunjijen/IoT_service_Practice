print('함수(function, method)-------------')
'''
# 함수 : 코드를 감싸고 있는 일정 영역. 기능을 수행한다.
# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈화
'''
#사용자 정의 함수 구성
'''
def 함수명([x,y,...])
    실행문
    [return x*y] #특정값을 반환하고자 할때 return문을 사용한다. return 함수블럭 마지막에 위치해야 함
'''
#[1] 매개변수 없고 반환값도 없는 함수
def print_star():
    for _ in range(5):
        print("★",end="")
    print()

    
# 함수 호출을 해야 함수가 실행된다
print_star()
print_star()
print_star()
print_star()

'''
함수의 인수로 전달하면
해당 인수만큼 반복돌면서 @출력하는 함수를 구성하세요
호출해보기
'''
#[2] 매개변수를 받는 함수. 반환값은 없다
def print_snail(num):
    for _ in range(num):
        print("@", end="")
    print()

print_snail(3)
print_snail(7)
print_snail(50)
#[2]  매개변수를 받는 함수. 반환값은 없다
'''
매개변수를 2개 받아서 특수문자를 n개출력하는 함수를
구성하고 호출해보세요
'''
def print_shape(ch, n):
    for _ in range(n):
        print(ch,end='')
    print()
print_shape("#",10)
print_shape("$",25)
print_shape("&",5)

'''
함수 구성 형태
[1] 매개변수 없고, 반환값도 없고
[2] 매개변수 있고, 반환값 없고
[3] 매개변수 없고, 반환값 있고
[4] 매개변수도 있고, 반환값도 있고
'''

#[3] 매개변수 없고, 반환값 있고
def myfunc():
    print('myfunc()입니다~')
    return 555  #함수를 호출한 쪽으로 값을 전달한다
myfunc()
myfunc()
money=myfunc()
print(money)
print(money*3)

def yourfunc(a,b,c):
    d=a+b+c
    return d

#yourfunc호출하기
x=yourfunc(1,2,3)
print('x=',x)
print(yourfunc(45.1,85.6,99))
print(yourfunc("Hello","Hi","Allo"))

print(x**3)

def hisfunc():
    pass

hisfunc()
print(hisfunc()) #None


'''
[문제1] 
cm => inch로 변환하는 함수를 구성해보세요
길이는 몇cm인가요? => 입력을 받으면
해당 cm에 해당하는 inch값을 출력하는 함수를 구성해보세요.
1cm =0.3937inch
함수명: convertInch
'''
def convertInch(cm):
    inch=cm*0.3937
    return inch

cm=float(input('길이는 몇 cm인가요? 인치로 변환할게요'))
i=convertInch(cm)
print(f'{cm}cm 는 {i} inch입니다')


'''
# [문제2]
# 2개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요.
함수: max1
'''
def max1(a, b):
    max(a, b)
    print(max(a, b))

max1(45,85)

def max11(a, b):
    if a > b:
        return a
    else:
        return b
mx=max11(25,121)
print('mx=',mx)

def max111(a,b):
    if b>a:
        a=b
    return a
print(max111(-12,-1))
'''
 [문제3]
# 4개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요.
'''
def max2(a, b, c, d):
    list1 = [a, b, c, d]
    re = 0
    for i in list1:
        if re < i:
            re = i
    return re

mx=max2(211,-8,22,31)
print('mx=',mx)

def max22(a,b,c,d):
    return max11(max11(max11(a,b),c),d)

mx=max22(456,852,753,951)
print('mx=',mx)