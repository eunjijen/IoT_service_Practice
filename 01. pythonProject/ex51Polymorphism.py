# ex51Polymorphism.py
print('--다형성--------')
'''
다형성(Polymorphism)
- 여러 가지 형태를 가질 수 있는 특성
- 같은 모양의 코드가 다른 동작을 하는 것 (메소드 오버라이드도 다형성의 한 예)
'''
class Flight:
    def __init__(self, name):
        self._name=name #_(언더바 1개)붙인 인스턴스 변수==>자식클래스에서 접근 가능함
        
    def fly(self):
        print('fly() 원형 메소드')
        #pass

class Bird(Flight):
    def __init__(self,name):
        self._name=name
    
    #메소드 오버라이드
    def fly(self):
        print(self._name,'이 훨훨 날아요~~')


class AirPlane(Flight):
    def __init__(self,name):
        self._name=name
    def fly(self):
        print(self._name,' 비행기가 슝슝 날아요~~')
class Test:
    def test(self):
        a1=AirPlane("드론")
        a1._name="비행기"

if __name__ =='__main__':
    '''
    Flight,Bird,AirPlane객체를 각각 생성한 뒤
    list에 저장하고
    for루프 이용해서 fly()호출하기
    '''
    f1=Flight("나는것들")
    f2=Bird("까치")
    f3=AirPlane("대한항공")
    f3._name="아시아나"
    arr=[f1,f2,f3, Bird("참새")]

    for f in arr:
        print('*'*20)
        f.fly()








