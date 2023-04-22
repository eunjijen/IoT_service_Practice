print("Hello Python")
#Ctrl+Shift+F10
print("Hi Python")
#Shift+F10

#단문 주석
"""
복문 주석
여러 라인을 주석 처리합니다
"""
'''
이것도 주석 입니다
'''
# print(출력할 문자열):문자열은 ' ' 또는 " "로 감싼다
# Ctrl+/ : 현재 커서 라인을 주석 처리한다
print('안녕 파이썬~~')
print('hi','hi','hi')
# help(print)
print('Hello', 'Hi', sep='#') #sep=' ' 구분자
print('Allo','Allo','Allo', end=' ') # end="\n": 줄바꿈을 나타내는 제어문자(escape문자)
print('Python')

print('Allo '*5)

print("Hello "+"World~")
'''
+ 연산자: 숫자유형일 때는 덧셈을 수행
         문자열 유형일때는 문자열 결합이 일어난다
'''

a=5
b=7
print(a+b)
'''
사칙연산자: +, -, *, /, 
// : 나누기를 수행하되 몫에서 정수부분만 취한다 
'''
print(a*b, a-b, b/a, a/b)

print(b/a, b//a) # 1.4  1

'''
"5+7=12 입니다" 를 출력해보세요
'''
print(a,'+',b,'=',a+b,'입니다')
print(str(a)+'+'+str(b)+'='+str(a+b)+'입니다')
'''
python 2.x 버전: format()함수를 이용
python 3.x 버전: % 형식 format 지정자 사용
'''
#2.x 버전 {}  : placeholder
print("{0}+{1}={2} 입니다".format(a,b,a+b))
print("{1}+{0}={2} 입니다".format(a,b,a+b))

#3.x 버전 : % 형식 format 지정자 사용
'''
%d : decimal 정수 표현
%f : float 실수 표현
%s : string 문자열 표현
'''
print('%d x %d = %d 입니다' %(a, b, a*b))
'''
7 / 5 = 1.4 입니다
'''
print('%d / %d= %.1f %s' %(b,a, b/a,'입니다'))

'''
%전체자리수.소수점이하자리수f
'''
pi=3.141592
print('%f' %pi)
'''
원주율을 전체 10자리 중에 소수점 아래 2칸만 출력해보기
원주율을 전체 10자리 중에 소수점 아래 3칸만 출력해보기
원주율을 전체 10자리 중에 소수점 아래 4칸만 출력해보기
'''
print('%10.2f' %pi)
print('%10.3f' %pi)
print('%10.4f' %pi)
print('%010.4f' %pi) #앞에 빈칸을 0으로 채운다

'''
3.8이후 : f-string
'''

print(f'{a} x {b} = {a*b}')
print(f'원주율은 {pi} 입니다 {pi:10.2f}')
price=250000
'''상품가격은 250000원 입니다'''
print(f"상품 가격은 {price:,}원 입니다")

'''
format()함수: {0},{1} ,
            key-value 형식으로 인자를 전달하는 방법도 있다
'''
print('위도:{}  경도: {}'.format('31.2N','120.0E'))
print('위도:{0}  경도: {1}'.format('31.2N','120.0E'))
print('위도:{lat}  경도: {long}'.format(long='120.0E',lat='31.2N'))


