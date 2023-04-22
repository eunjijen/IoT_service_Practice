import threading
import requests, time

class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
        self.daemon = True  # 데몬 스레드 설정, 디폴트는 false

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)


t = HtmlGetter('https://google.com')
# t.daemon = True   # 이걸로도 설정 가능 start 이전에 설정해주면 돼
t.start()

# t.join()  # t 스레드가 끝날때까지 대기
print("### End ###")
