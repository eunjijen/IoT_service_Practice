from threading import Lock

class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = "아무개"
        self.address = "모름"
        self.lock = Lock()

    def across(self, name, address):
        self.lock.acquire()
        # critical section##################
        self.counter += 1
        self.name = name
        self.address = address
        self.check()
        # 이순신이 address까지 통과했는데 임꺽정이 name까지 통과하면
        # name은 임꺽정, address는 이순신의 주소가 되어 일치하지 않음이 뜬다 - 공유자원을 이용할 때 일어남
        ###############################################################
        self.lock.release()

    def toString(self):
        return "이름: {}, 출신:{}, 도전 횟수: {}".format(
            self.name, self.address, self.counter
        )
    
    def check(self):
        if self.name[0] != self.address[0]:
            print("문제 발생!!!" + self.toString())