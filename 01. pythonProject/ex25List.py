print('--list 활용 문제---------')
'''
전체 평균 점수 구하기
'''
'''
40점 미만의 점수일 경우 과락
시험은 전체 평균 점수가 60점 이상일 때 통과
--------------------
각 과목 점수 출력
과락한 과목수
'''

title=['국어','영어','수학','물리','화학','한국사']
score=[55,88,75,41,35,50]
'''
국어: 55
영어: 88
...
총점: xx
평균점수: xx
-------------
Test결과
40점 미만 과목수: 1, 과락 과목명: 화학
안타깝지만 불합격입니다
list에 적용가능한 내장함수: sum(), max(), min(), sorted(), len()...
'''
title = ['국어', '영어', '수학', '물리', '화학', '한국사']
score = [78, 88, 79, 88, 90, 100]
avg = sum(score) / len(score)  # 평균점수
f_title = []  # 과락 과목
count = 0  # 과락 과목 수

for i in range(len(title)):
    print(f'{title[i]} : {score[i]}')
    if (score[i] < 40):
        count += 1
        f_title.append(title[i])

print('-' * 20)
print('-----Test결과--------------')
print('평균점수:', avg)
print(f'과락한 과목수: {count}', f'과락한 과목명: {f_title}')
if (len(f_title) > 0 or avg < 60):
    print('안타깝지만 .. 불합격입니다')
else:
    print('합격입니다!')


#--------------------------------------
member = ['정우람','박으뜸','배힘찬','천영웅','신석기','배민규','전민수','김건우','박찬호','이승엽']
#[1] 이름 가나다 순으로 정렬해 출력하세요
lst=member[:]
lst.sort()
print(lst)
print(member)
#[2] 회원 중 '신석기' 회원을 탈퇴시키세요
lst.remove('신석기')
print(lst)
#[3] 신입회원 '도지원'을 추가하세요
lst.insert(1, '도지원')
print(lst)
#[4] 정우람 회원을 정빛난 으로 변경하세요
# lst.insert(8, '정빛난')
# lst.remove('정우람')
# print(lst)
lst[lst.index('정우람')]='정빛남'
print(lst)
#중첩 리스트
score=[88,45,65,77,99,100] #1차원 리스트
matrix=[1,2,score,3]
print(matrix[0]) #1   scalar 값
print(matrix[1])
print(matrix[2]) # list

'''
반복문 이용해서 matrix에 저장된 값 출력하기

for 인덱스, 값 in enumerate(list):
'''
for i, val in enumerate(matrix):
    if i==2:
        for k in val:
            print(k, end=' ')
    else:
        print(val, end=" ")
print()

arr=[[1,2,3],['하나','둘','셋']] #중첩 리스트

print(arr[0]) #[1,2,3]
print(arr[1]) #['하나','둘','셋']
print(arr[1][1]) # 둘  arr[행의인덱스][열의인덱스]
print('-'*20)
#[1]
for val in arr:
    # print(val)
    for x in val:
        print(x, end=' ')

print('-'*20)
#[2]
for x, y, z in arr:
    print(x,y,z, end=' ')

# for in range()
print('\n','-'*20)

for i in range(len(arr)): #행의 크기
    for j in range(len(arr[i])): #열의 크기
        print(arr[i][j], end=' ')
print()

'''
중첩 리스트를 이용해 아래와 같은 형태의 데이터를 저장한 후 출력하기
[
    [1	6	11	16	21]
    [2	7	12	17	22]
    [3	8	13	18	23]
    [4	9	14	19	24]
    [5	10	15	20	25]
]
for루프 이용하기 중첩리스트에 저장한 뒤

중첩 for루프 이용해서 출력하세요
'''
lst=[]
arr=[]
for i in range(5):
    arr=[]
    for j in range(5):
        arr.append(i+1+5*j) #1차원 리스트
    lst.append(arr) #2차원 리스트
print('-'*20)
print(lst)

for x,y,z,a,b in lst:
    print(x,y,z,a,b)