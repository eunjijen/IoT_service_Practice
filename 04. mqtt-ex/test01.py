import requests

res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=seoul&APPID=37f2c07792dd5e7be399b70beb6fa34f&lang=kr")
print(res.status_code)   # 200
print(res.text)

weather = res.json()  # 사전으로 변환
print(weather["main"])
