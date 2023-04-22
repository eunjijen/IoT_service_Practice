import time

def clock(mode):
    while mode>0:
        seconds=time.time()
        ltime=time.localtime(seconds)
        print(time.strftime("%H시 %M분 %S초", ltime))
        time.sleep(1) #1초간 중지
    else:
        print('시계가 고장났어요~')

def sayHello(name="아무개"):
    print('-'*20)
    print("Hello? ", name)
    print('안녕하세요? ', name,'님~')
    print('-' * 20)

import datetime as dt

def printToday():
    today=dt.date.today()
    print(today)
    
#단위 테스트  현재 파일이 메인 프로세서라면 아래 함수를 실행하라...
if __name__=='__main__':
    clock(-10)
    sayHello("홍길동")
    printToday()