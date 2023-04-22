# ex30Comprehension
print('--zip()활용-------------')
'''
zip(): aggregation을 수행한다
'''
a=[10,20,30]
b=['ten','twenty','thirty']

print(a)
print(b)

for c in zip(a,b):
    print(c)


str_list=['hello','world','python','good']
int_tuple=(1,2,3)
int_list=[100,200,300,400,500]
'''
zip() 이용해서 집적화를 한 뒤
for루프 이용해서 출력하세요
1:1로 매칭이 되지 않을때 어떻게?==> 매칭되지 않는 요소들을 버린다
'''
for v in zip(str_list, int_tuple, int_list):
    print(v)
'''
zip()으로 묶여진 튜플을 unpacking하려면?
: zip()함수에 묶인 자료를 인자로 넘기고 *연산자를 앞에 붙여준다
'''
zlist=list(zip(str_list,int_tuple,int_list))
print(zlist)

a,b,c =zip(*zlist)
print(a,b,c)

print('---comprehension-------------')
'''==============================================================
# 컴프리헨션comprehension - 반복문 축약
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능
'''
'''
리스트 내포(List comprehension)란 list 안에서 for와 if를 사용하는 문법을 의미한다. 이를 사
용하면 매우 직관적인 코딩이 가능하다. 다음은 리스트 내포의 첫 번째 형식으로 리스트와 for문을 동
시에 이용하여 리스트 안에서 반복을 수행하는 명령문을 처리할 경우 사용된다
[형식1]========================================================
변수 = [실행문 for 변수 in 열거형 객체]
=>위 형식의 프로그래밍 처리 과정은 ① for문에서 열거형객체의 원소 하나를 변수로 넘겨 받는다. ②
변수에 할당된 값을 실행문으로 처리한다. ③ 처리된 결과를 변수에 순차적으로 추가(append)한다.

[형식2]========================================================
변수 =[실행문 for 변수 in 열거형객체 if 조건식]
=>위 형식의 프로그래밍 처리 과정은 ① for문에서 열거형객체의 원소 하나를 변수로 넘겨 받는다. ②
변수에 할당된 값을 조건식으로 사용하여 비교 판단한다. ③ 조건이 참(T「ue)이면 변수에 할당된 값을
실행문으로 처리한다. ④ 처리된 결과를 변수에 순차적으로 추가(append)한다
'''
nums=[1,2,3,4,5,6,7,12]
evens=[]
for v in nums:
    if v%2==0:
        evens.append(v)
print(evens)

odds=[ v for v in nums if v%2==1] #list comprehension
print(odds)

# 1 ~ 10 까지 제곱값을 리스트로 생성하는 축약문을 작성하세요
'''
[1,4,9,16...100]
[1]
변수=[표현식 for 항목 in 반복가능객체]
'''
lst=[ v**2  for v in range(1,11)]
print(lst)
'''
[2] for if 축약문
변수=[표현식 for 항목 in 반복가능객체 if 조건식]
'''
lst2=[8,12,7,'A',True, False]
'''
lst2리스트에 저장된 값들의 제곱값을 구해 새로운 리스트에 저장하세요 =>축약문이용하기
문자열일 경우 에러발생 ==> 조건걸기 int형일때만 거듭제고값을 구해 리스트에 담기
'''
lst3=[v**2 for v in lst2 if type(v)==int]
print(lst3)
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

'''
변수= 표현식1 if 조건식 else 표현식2
[3] for 다중if 축약문
변수 = [ 표현식1 if 조건식 else 표현식2  for 항목 in 반복가능객체  ]
-----------------------------
# 1 ~ 100 사이의 정수 중 임의의 정수가 짝수면 'even',
# 홀수면 'odd' 라고 구분해서 리스트에 저장하세요
# [odd even odd even ...]
'''
plus3=["even" if v%2==0 else "odd" for v in range(1,101)]
print(plus3)
'''
변수=[표현식 for v1 in 객체1
                for v2 in 객체2]
구구단 2단, 3단의 결과값들을 gugu라는 변수 리스트 형태로 포함시키세요
'''

gugu = [f'{i} * {j} = {i * j}' for i in range(2, 10)
                for j in range(1,10)]
print(gugu)
for v in gugu:
    print(v)
'''
딕셔너리 for  comprehension
변수={ key:value표현식 for k,v in zip(반복객체1, 반복객체2)}
'''

'''
# 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 값은 합격여부로 하는 딕셔너리를 생성하세요
# 단, 국어점수가 80점이상인 경우 '합격',
#     그외는 '불합격'이라고 출력함
'''
std = ['철수','영희','길동','꺽정']
kor = [50,80,90,60]

result=["합격" if v>=80 else "불합격" for k,v in zip(std, kor) ]
print(result)

result2={k:"합격" if v>=80 else "불합격" for k,v in zip(std,kor)}
print(result2)