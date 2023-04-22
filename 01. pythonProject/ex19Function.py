print('--함수----------')
lst=[1,2,3,4]
lst[0]=100
print(lst)
tup=(1,2,3,4)
#tup[0]=1000 #튜플은 불변성(immutable)을 갖는다
print(tup)
'''
가변 매개변수
매개변수 앞에 *을 붙인다
=> 가변 매개변수에는 함수에서 전달한 모든 인수가 튜플(tuple) 형태로 전달된다
'''

def addNums(*nums):
    tot=0
    for i in nums:
        tot+=i
    print(nums, type(nums))
    print('tot=',tot)
    return tot

addNums(1,2,3)
addNums(11,22)
addNums(11,22,33,44,55)

'''
#매개변수로 딕셔너리(key=value형태로 저장하는 자료구조) 전달시
#가변 매개변수로 딕셔너리를 사용하려면
#두개의 별 ** 기호를 사용하여 선언해야 한다.
list => []
tuple => ()
dict =>{ }
'''

def printMap(**dicts):
    print(dicts, type(dicts))
    for key in dicts:
        print(key,'=>',dicts[key])
printMap(one=1, two=2, three=3)

print('#'*30)
'''
인자 전달 방식
[1] 디폴트 인자: 함수를 호출할때 함수에 디폴트값(기본값)을 지저하여 인자에서 사용하도록 하는 방식
[2] 키워드 인자: 함수를 호출할때 값만 전달하는 것이 아니라, 인자의 이름을 함께 명시하여 전달하는 방식
'''
def addPrint(a=100,b=200):
    print(f'{a}+{b}={a+b}')
    return a+b

addPrint(11,33)
addPrint()
#TypeError: addPrint() missing 2 required positional arguments: 'a' and 'b'

#print(value, sep=" ", end="\n")

addPrint(b=7,a=2)


def gop(a,b=3,c=5): #a는 기본값이 없으므로 반드시 값으로 전달해야 함
    print(a*b*c)

gop(10)
#gop() #[x]
gop(2,4)
gop(c=11, b=22, a=2)

'''
[1]
#이름 나이 주소를 매개변수로 받아서 출력하는 함수를 만들고
#매개변수가 없을 경우 기본값을 주세요
함수명: info()
'''
def info(name='아무개', age=20, address='마포구'):
    print(f'''
    이름: {name}
    나이: {age} 세
    주소: {address}
    ''')
info('김철수',23,'강남구 도곡로')
info()
'''
[2]
직사각형 또는 원의 면적을 구하는 함수를 구성하시오.
첫번재 인자값이 0이면 사각형 면적을, 1이면 원의 면적을 구하시오.
함수명: area(mode, w, h, r)
'''
import math
print(math.pi)

def area(mode, w=1, h=1,r=1):
    if mode==0:
        print(f'가로: {w}  세로:{h} 인 사각형 면적: {w*h} ')
        return w*h
    elif mode==1:
        y=math.pi*r*r
        print(f'반지름이 {r}인 원의 먼적: {y:.2f}')
        return y
    else:
        print('인자값이 잘못되었습니다. 사각형:0, 원:1')

area(0,5,8,1)
area(1, r=12)
area(0,14,7)

'''
보통 다른 언어들은 함수에서 1개의 값만 반환한다
파이썬의 경우는 return문에 2개 이상의 값을 반환할 수 있다.
==> 이 값을 받는 변수의 자료형은 tuple 유형이된다
'''

def calc(a,b):
    hap=a+b
    mins=a-b
    gop=a*b
    div=a/b
    return hap, mins,gop,div

# calc호출하기 반환값을 변수로 받아 출력하기
y=calc(12,34)
print(y, type(y))
#unpacking
a1,a2,a3,a4=calc(3,2)
print(a1,a2,a3,a4)
