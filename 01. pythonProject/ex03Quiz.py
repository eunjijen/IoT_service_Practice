#사용자로부터 값 입력받기: 변수 = input('메시지')
name=input('당신의 이름을 입력하세요: ')
print('name: ',name)
'''
[1] 나이를 입력받아 변수에 대입한 뒤에
현재나이: 22 세
10년뒤 나이: 32 세 
'''
age =input('나이를 입력하세요=>')
print('현재 나이: ',age, type(age))
print('10년 뒤 나이: ',int(age)+10) # str+int [x]   int(str)+int

#[2] 국어, 영어, 수학 점수를 입력받아
# 총합계 점수와 평균을 출력하는 코드를 작성하세요
kor =float(input('국어 점수=>'))
eng =float(input('영어 점수=>'))
math = float(input('수학 점수=>'))
total=kor+eng+math
avg=total/3
print(f'''
국어: {kor}점
영어: {eng}점
수학: {math}점
---------------
총합: {total}점
평균: {avg} 점
''')

'''
[3]
이메일, 아이디, 비밀번호, 이름을 입력받아 아래와 같은 형태로 출력하세요
-----------------
To. hong@naver.com
▶️아이디및 비밀번호 확인'
 홍길동 고객님 안녕하세요.
 홍길동  고객님의 아이디와 비밀번호는 아래와 같습니다.
 아이디 : hong
 비밀번호 : 123
 ---------------------
'''
email=input('이메일: ')
uid=input('아이디: ')
upw=input('비밀번호: ')
name=input('이  름: ')

strVar=f'''
To. {email}
{name}고객님 안녕하세요?
{name}님의 아이디와 비밀번호는 아래와 같습니다
아이디: {uid}
비밀번호: {upw}
'''
print(strVar)