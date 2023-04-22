print('--class member들----')
'''
클래스의 구성원
    [1] 멤버변수
        <1> 인스턴스 변수
        <2> 클래스 변수
    [2] 사용자정의메소드
    [3] 생성자 : 객체가 생성될때 자동으로 호출된다 __init__()
                역할: 멤버변수의 값을 초기화하는 역할을 수행한다
    [4] 소멸자 : 객체가 메모리에서 해제될때 자동으로 호출된다 __del__()
                하지만 파이썬에서는 자동으로 메모리 관리를 하므로 자주 사용되지는 않는다
'''
class Cat:
    sound="야옹 야옹~~" #멤버변수
    '''
    멤버변수
        -인스턴스 변수: self.변수(내부에서 참조시)
                      객체명.변수  
        -클래스 변수 : cls.변수
                    클래스명.변수
    '''
    def __init__(self, n="",age=1, breed=""):
        print('__init__ 생성자 함수 호출됨...')
        self.name=n
        self.age=age
        self.breed=breed
    def __del__(self):
        print('__del__소멸자 함수 호출됨...')
        del self.name
        del self.age
        del self.breed

    def show(self):
        print('~'*20)
        print('고양이 종류: ',self.breed)
        print('이  름  : ',self.name)
        print('나  이  : ',self.age)


if __name__ =='__main__':
    c1=Cat("예쁜이",1,"페르시안")
    c1.show()

    c2=Cat("까미",2,"코숏")
    c2.show()
    '''
    __init__()형태에 맞게 객체를 생성해야 한다.
    '''
    c3=Cat()
    c3.name="하양이"
    c3.age=3
    c3.show()





