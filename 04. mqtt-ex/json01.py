import json

# json.loads(string) --> dict
# json.dumps(dict) --> string

control = {
    "led" : 1,
    "servo" : 45
}

msg = json.dumps(control)

print(msg, type(msg))
# {"led": 1, "servo": 45} <class 'str'> key는 큰 따옴표
# print(msg["led"]) --> 에러

print(control)
# {'led': 1, 'servo': 45}
print(control["led"])  # 1
print('------------------------------------')

control2 = json.loads(msg) # 문자열 --> 사전
print(control2, type(control2))
# {'led': 1, 'servo': 45} <class 'dict'>

# http://api.openweathermap.org/data/2.5/weather?q=seoul&APPID=37f2c07792dd5e7be399b70beb6fa34f&lang=kr
