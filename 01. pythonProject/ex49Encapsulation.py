print('---Account계좌를 만들어 캡슐화 연습하기----')
'''
 [1] 멤버변수를 캡슐화해서 money, name, accNo 를 선언하기
 [2] 생성자 함수 구성하기
 [3] 캡슐화된 변수를 접근하는 setter, getter메소드를 각각 구성하세요
 [4] 객체 생성해서 변수값들 출력해보고, 메소드도 호출해보기
'''
class Account:
    def __init__(self, money, name, accNo):
        self.__money = money
        self.__name = name
        self.__accNo = accNo

    def getVar(self):
        return self.__money, self.__name, self.__accNo

    def setVar(self, m, n, a):
        self.__money = m
        self.__name = n
        self.__accNo = a

if __name__ == '__main__':
    a1 = Account(10000, '호식', '435-354-235')
    print(a1.getVar())
    a1.setVar(50000, '후식', '34-42525-3456')
    print(a1.getVar())

    #print(a1.__money) [x]