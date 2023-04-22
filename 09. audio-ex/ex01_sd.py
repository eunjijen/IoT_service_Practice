import sounddevice as sd

duration = 5.5 # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata    # 스피커 출력

with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))


# input overflow, output underflow
# underflow - 버퍼를 다 채우지 못함