# [1] 매출액과 매입액을 입력받아 총 수익을 출력하시오
# input()함수 이용
outcome=input('매출액을 입력하세요')
income=input('매입액을 입력하세요')
print('매출액: {}'.format(outcome))
print('매입액: {}'.format(income))
print('수익금: {}'.format(int(outcome)-int(income)))

# [2] 가로, 세로 길이를 입력받아 직사각형의 넓이를 구하시오
width=int(input('가로 길이 입력: '))
height=int(input('세로 길이 입력: '))
print(f'''
가로: {width}, 세로: {height}인 직사각형 면적: {width*height}
''')
# [문제3] 키와 몸무게를 입력받아 bmi지수를 계산하세요.
'''
-------------------------------------------
비만도 측정(BMI지수)
BMI를 이용한 비만도 계산은 자신의 몸무게를 키의 제곱으로
나누는 것으로 공식은 kg/㎡. BMI가 18.5 이하면 저체중 ／
18.5 ~ 22.9 사이면 정상 ／ 23.0 ~ 24.9 사이면 과체중 ／
25.0 이상부터는 비만으로 판정.
신체질량지수
(BMI) = 체중(kg)/[신장(㎡)]
-------------------------------------------
'''
weight=int(input('체중 입력: '))
height=int(input(' 키 입력: '))
BMI = weight/(height/100)**2
print(f'''
체 중: {weight} kg
신 장: {height} cm
BMI : {BMI:.2f}
''')

