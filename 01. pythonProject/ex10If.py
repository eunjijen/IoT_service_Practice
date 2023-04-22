print('if문------')
'''
[1]
2자리 정수를 입력받으세요
11 22 33 44 ...
10의 자리와 1의 자리가 같으면 "OK 10의 자리와 1의 자리가 같아요"를 출력
그렇지 않으면 "No 10의 자리와 1의 자리가 달라요" 출력
'''
Num = int(input("2자리 정수를 입력하시오 : "))
if Num//10 == Num%10 :
    print("10의 자리와 1의 자리가 같아요!")
else :
    print("10의 자리와 1의 자리가 달라요!")
# 삼항연산자
# 변수 = 참값 if 조건식 else 거짓일때 값
result ="10의 자리와 1의 자리 Same" if Num//10==Num%10 else "10의 자리와 1의 자리가 Not Same"
print(result)
'''
[2]
국어,영어,수학 점수를 입력받아서
합계 점수 출력
평균 점수 출력
학점 출력
if ~ elif ~ 이용하기
100~ 90점대: A
80점대: B
70점대: C
60   : D
그외  : F

[3] 위 입력한 과목 중 최소 점수를 맞은
과목과 점수를 출력해 보여주세요
'''
korean = int(input('국어: '))
english = int(input('영어: '))
math = int(input('수학: '))

total = korean + english + math
average = total / 3
print(f'합계: {total}')
print(f'평균: {average:.1f}')

if 80 <= average <90 :
    print('학점 B')
elif 90 <= average <=100:
    print('학점 A')
elif 70 <= average <80:
    print('학점 C')
elif 60 <= average <70:
    print('학점 D')
else:
    print('학점 F')
    
#최소값 구하기
mn=korean
s='국어'

if mn>english:
    mn=english
    s='영어'
if mn>math:
    mn=math
    s='수학'

print('최소 점수를 맞은 과목은 %s이며, 최소 점수는 %d 점입니다' %(s, mn) )