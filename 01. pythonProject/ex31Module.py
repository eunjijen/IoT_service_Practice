print('---module사용하기-----')
'''
모듈이란?
함수, 클래스들을 용도별로 모아 작성해놓은 파일
작성된 모듈을 사용하려면 해당 모듈을 메모리에 적재해야 함
import 문을 이용해서 모듈을 불러올 수 있다.
import 모듈명(파일명)
'''
#표준 모듈 확인
import sys
print(sys.builtin_module_names)
print('#'*50)

import math
print(dir(math))
print(math.factorial(5))
print(math.pi)
print(math.pow(2, 8)) #2의 8승
print(math.ceil(3.00001)) #올림값(정수)
print(math.floor(3.00001)) #내림값(정수)
print(math.sqrt(64)) #제곱근 값을 반환
print(round(3.1234)) #반올림 (소수점 첫째짜리)
print(round(3.1256, 2)) #소수점 3째자리 값에 의해 2째 자리를 반올림한다 3.13
print('---datetime모듈-------')
import datetime
# help(datetime)
print(datetime.datetime.now()) #현재 날짜 시간을 출력
#모듈명.클래스명.함수
print(datetime.date.today()) #오늘 날짜
tdy=datetime.date.today()
print(tdy.year,'년')
print(tdy.month,'월')
print(tdy.day,'일')
#요일 정보 weekday()
a=['월','화','수','목','금','토','일']
print(a[tdy.weekday()],'요일') # [월:0 ~ 금:4, 토:5, 일:6]

'''
import 모듈명 as 별칭
'''
import datetime as dt
stime=dt.datetime.now()
print(stime)
'''
날짜변경: replace()함수를 이용한 뒤 재할당한다
'''
stime=stime.replace(year=2023,month=5, day=5)
print(stime, a[stime.weekday()])
'''
남은 시간 구하기
datetime-datetime
'''
gap=stime-dt.datetime.now()
print('5월 5일까지 {}일 남았어요'.format(gap.days))

'''
오늘 부터 100일후 경과된 날짜 구하기
datetime 모듈의 timedelta 클래스를 이용해서 +,-연산자를 사용하여 구할 수 있다.
'''
day100=dt.timedelta(days=100)
print(day100, type(day100))

#100일 뒤
after100=dt.datetime.now()+day100

#100일 전
before100=dt.datetime.now()-day100

print(f'100일 뒤: {after100}, 100일 전: {before100}')

'''
현재 시간으로 부터 3시간 뒤를 출력하세요
'''
hour_3 = dt.timedelta(hours=3)
print(f'현재 시각 : {dt.datetime.now()}\n3시간 뒤 : {dt.datetime.now() + hour_3}')
print('-'*50)

import time
'''
시간 관련 정보를 제공하는 모듈
1970년 1월 1일 0:0:0 기준으로 지금까지 경과한 시간을
100만분의 1초 단위로 기록하고 저장하는 체계를 갖는다.
'''
seconds=time.time()
print(seconds)
#현재 시간으로 변경하려면  1년을 초단위로 계산
unit=60*60*24*365
cyear=seconds//unit
print(int(cyear)+1970,'년')

local_time=time.localtime(seconds)
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

def clock():
    while True:
        seconds=time.time()
        ltime=time.localtime(seconds)
        print(time.strftime("%H시 %M분 %S초", ltime))
        time.sleep(1) #1초간 중지

clock()