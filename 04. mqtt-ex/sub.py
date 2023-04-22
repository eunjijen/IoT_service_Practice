import paho.mqtt.client as mqtt

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdate, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        client.subscribe("iot/#")  # 연결 성공시 토픽 구독 신청
    else:
        print('연결 실패: ', rc)

# 관련 토픽 메시지 수신 콜백 함수
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())  # byte array --> str
    print(f" {msg.topic} {value} ")


# mqtt 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try:
    # 브로커 연결
    client.connect("localhost")

    # 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
    client.loop_start()   # 또는 loop.start()

except Exception as err:
    print('에러 : {err}')