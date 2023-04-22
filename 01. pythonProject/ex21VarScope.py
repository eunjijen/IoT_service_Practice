print('---Varaible Scope-------')
'''
변수의 유효범위(scope)
    - 전역변수 (global varaiable) : 전역에서 사용가능함
    - 지역변수 (local variable)   : 특정 블럭 내에서만 사용 가능함
'''
name='전역변수'

def foo():
    aaa=100 #지역변수
    print('---foo()-----')
    print('name: {}'.format(name))
    print('aaa: {}'.format(aaa))

foo()
# print('aaa변수값은? ', aaa)
#aaa: foo()함수 안에서만 사용할 수 있는 지역변수
print('name변수값은? ',name)
var='@@@' #전역변수
def demo():
    # var='local_var' #지역변수
    global var  # 함수 영역 밖에서도 선언한 변수를 사용하고 싶다면 global 을 붙여 선언하자. 그러면 전역변수가 된다
    var='global_var'
    print(var) #global_var

demo()
print('#'*30)
print(var)
print('-'*50)

def print_sum():
    # global a
    # global b
    a=100# 지역변수
    b=200
    print(f'print_sum() 내부: {a}와 {b}의 합은: {a+b} 입니다') # 100  200  300

a=10 #전역변수
b=20
print_sum()
result=a+b
print(f'print_sum() 외부: {a}와 {b}의 합은: {a+b} 입니다')