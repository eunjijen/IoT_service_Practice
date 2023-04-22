print('--tuple----------')
# help(tuple)
'''
[1] 튜플
- 입력 순서를 기억한다
- 데이터 중복 저장 가능
- 저장된 데이터를 변경할 수 없다(불변성)
메소드
    -  count(x) : 튜플 내에 특정 값 x가 몇 개 있는지 반환
    -  index(x) : x값의 위치 인덱스 번호를 반환함
'''
t1=() #빈 튜플
t2=(100) #튜플이 아니라 int형
t3=(100,) #1개의 요소를 저장하려면 반드시 쉼표(,)를 넣어주자
t4=('N','e','w','N','I','C','E') #문자 튜플
t5=10,20,30,'Hello' #혼합 튜플
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))

print('t4내에 N의 갯수: ',t4.count('N'))
print("N의 index는: ",t4.index('N')) #맨 앞에 있는 N의 인덱스를 반환함
'''
index()함수는 찾는 값이 없을 경우 ValueError를 발생시킨다.=> 별도의 에러 처리 문장이 필요함
'''
try:
    print('X의 index는: ',t4.index('X')) #ValueError: tuple.index(x): x not in tuple
except:
    print('X는 t4튜플 내에 없습니다')

'''
튜플 조회 (R)
'''
print('t5[3]=',t5[3])
'''
튜플 수정? [x] 변경 불가, 추가, 삭제도 안된다
'''
# t5[3]='Hi' # TypeError
# t5.append('Hi')

'''
packing, unpacking
[1] packing : 하나의 변수에 여러 개의 값을 넣는 것
[2] unpacking : 패킹된 변수에서 여러 개의 값을 꺼내는 것
'''

a=(100,200) #packing
print(a[0], a[1])

#unpacking
x, y =a
print('x=',x)
print('y=',y)

#list unpacking
lst=['A','B','C','D']
a, b, *c=lst
print(a,b)
print(c)

'''
tuple의 +와 * 연산
[1] + : 튜플 요소들을 서로 연결하여 하나로 합친다
[2] * : 튜플의 반복 연산을 수행함
'''
print('t3=',t3)
print('t4=',t4)
print('t3+t4=',t3+t4)

t7=t3*5
print(t7) #(100, 100, 100, 100, 100)
'''
만약에 튜플의 요소를 변경하고 싶다면? [x]
- tuple=> list로 변환   list()
- list의 요소값을 변경한다  
- list=> tuple로 변환한다 tuple()
'''
arr=list(t7)
print(arr, type(arr))
arr[1]=200
arr[2]=300
print(arr)
t7=tuple(arr)
print('t7=',t7)



'''[1]
(1919,3,1) 튜플을 생성하시오
그런뒤 unpacking을 통해 year,month,day변수에 할당후 아래와 같이 출력하시오
1919년 3월1일은 삼일절 입니다.
'''
birth = 1919, 3, 1
year, month, day = birth
print(f'{year}년 {month}월{day}일은 삼일절 입니다.')

'''[2]
# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
'''
import random as rnd
lst1 = []
tup1 = ()
for i in range(6):
    lst1.append(rnd.randint(1, 45))
tup1 = tuple(lst1)
print(lst1)
print(tup1)
'''
[3] lotto번호를 랜덤하게 6개 생성해서
tuple에 저장한 뒤 해당 튜플을 출력하세요 (단, 동일한 숫자는 없어야 합니다)
'''
lst2 = []
tup2 = ()
while len(lst2) < 6:
    r = rnd.randint(1, 45)
    if lst2.count(r) == 0:
        lst2.append(r)

tup2 = tuple(lst2)
print(tup2)

#함수의  return문과 tuple
import math
def area_circum(radius):
    area=math.pi*radius**2
    cir=2*math.pi*radius
    return area, cir

tup3=area_circum(10)

print(tup3, type(tup3))




