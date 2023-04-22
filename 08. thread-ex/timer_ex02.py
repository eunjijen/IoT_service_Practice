import threading
from time import sleep

def do_something():
    print('time out!')

timer = threading.Timer(2, do_something)  # 2초뒤에 가동되게
timer.start()

sleep(1)
timer.cancel() # 타이머 중단

# 현재 시점에서 2초 연장
# 바로 start시키면 안됨 timer를 다시 생성해서 start 시커야돼 
timer = threading.Timer(2, do_something)
timer.start()

print('Main Thread Exit')