class Dog:
    sound="멍멍~~"
    def __init__(self, name=None,age=None, breed=None):
        self.name=name #캡슐화되지 않은 인스턴스 변수
        self.age=age
        self.__breed=breed #캡슐화==> 내부클래스에서는 접근할 수 있으나 외부의 다른 클래스에서는 접근 불가
    #getter
    def getBreed(self):
        return self.__breed

    #setter
    def setBreed(self, b):
        self.__breed=b
'''
멤버변수 앞에 _(underbar)기호를 연속해서 2개 넣으면 외부에서 접근이 불가능한 은닉변수가 된다
'''        