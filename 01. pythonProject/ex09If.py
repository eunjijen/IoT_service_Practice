#[1] 입력받은 정수값의 홀 짝을 판별하는 프로그램을 작성하세요
number = int(input("정수를 입력하시오"))
if number%2==0:
    a="짝수"
else:
    a="홀수"
print(f"정수는 {a}입니다.")
'''
[2]
price=10000
나이를 입력받아 20세 미만이면 10%를 할인하여 가격을 알려주세요
'''
price=25000
age=int(input('나이를 입력하세요: '))
if age<20:
    # price=price- price*10/100;
    price=price*0.9  #   정수 * 실수 ==>실수
print('영화 관람 가격은 ',int(price),"입니다")

# [문제 3]
# 0~9999 사이의 정수가 몇 자리인지 알려주세요.
# 15  -->  2  123--->3  7777-->4
val=int(input('숫자를 입력하세요. '))
if 0 <= val < 10 :
    s = 1
elif 10 <= val < 100 :
    s = 2
elif 100 <= val < 1000 :
    s = 3
elif 1000 <= val < 10000:
    s = 4
print(s)

if val//10==0:
    s="1자리수"
elif val//100==0:
    s="2자리수"
elif val//1000==0:
    s="3자리수"
elif val//10000==0:
    s="4자리수"
print(s)