print('---예외 처리----')
'''
# 예외처리
# 프로그램을 만들다 보면 수많은 에러가 발생함
# 코드를 잘못 작성하거나, 실행상의 문제로 인해
# 에러가 발생하면 프로그램 실행이 중단되기도 함
#
# 하지만, 프로그램이 중단되는 것을 피하기 위해
# 이러한 에러는 무시하고 넘어가줬으면 하는때도 있음
# 에러에 따른 적절한 처리를 하고 싶을때도 있을 것임
#
# 파이썬에서는 try-catch-except 구문으로
# 예외처리를 할 수 있음
#
# error와 except 차이 비교
# 에러 : 프로그램 실행 중 오작동이나 비정상적 종료를
# 유발하게 하는 원인
#
# 예외 : 개발자가 완전히 조치할 수 없지만
# 어느정도 수습할 수 있는 수준의 덜 심각한 오류
# 예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음
-------------------------
파이썬에서는 예외처리 프로그램 로직을 작성할 수 있도록 다음과 같은 형식으로 try ~ except
finally 블록을 제공한다. try 블록은 예외가 발생할 가능성이 있는 코드를 작성하는 영역이고,
except 블록은 예외가 발생할 경우 예외를 적절하게 처리하는 코드를 작성하는 영역이다. 
finally 블록은 예외와 상관없이 무조건 처리할 코드를 작성하는 영역으로 생략이 가능하다.
--------------------------

예외처리
try:
    예외발생 가능 코드
except 예외명  as 변수명:
    예외처리코드
else:
    try절에서 예외가 발생하지 않았을 경우 실행될 코드
finally:
    반드시 실행해야 할 코드
 '''
print('---프로그램 시작-------')
try:
    n=int(input('정수를 입력하세요: '))
    print(f'10/{n}={10/n}')
    arr=[10,20,30]
    print(arr[n])
except ZeroDivisionError as ex1:
    print('Error: 입력값에 오류가 있습니다 0이 분모가 되어선 안돼요!!', ex1)
except IndexError as ex2:
    print(f'Error: 리스트의 인덱스 값은 {len(arr)-1}까지 가능합니다!! ',ex2)
print('>>반드시 실행되어야 할 코드<<')
print('---프로그램 끝----------')







