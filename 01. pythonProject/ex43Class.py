print('---class와 instance-----')
'''
객체지향 프로그래밍(Object Oriented Programming)-OOP언어 : Python, Java, C++, C#...
- 현실 세계에 존재하는 객체를 프로그래밍 세계로 끌어들인 것
- 객체란?
    유무형의 사물
    <1> 속성 ==> 멤버변수로 표현한다 "has a"관계를 갖는다
    <2> 행동양식==>동사형. 메소드로 표현한다
    
ex) 부동산 관련 프로그램
    - 매도자, 매수자
    - 집
    - 중개인
    ...
    ==>프로그램 세계로 끌어들인다 ==> class로 구성한다
-----syntax--------------------------
class  클래스명:
    멤버변수
    
    def 메소드명(self):
        ...기능..(행동양식)
-------------------------------------
클래스                 객체(instance,object)
-----------------------------------------
설계도                    구현물: 설계도에 의해 지어진 집=>객체
붕어빵틀                    붕어빵
--------------------------------------------
집, 학생, ==> Object, Instance
클래스들을 객체로 생성해서 메모리에 올리면 => 이것을 객체,insance,object라고 한다            
'''
class House:
    room=2  #멤버변수  House has a room
    owner='아무개'
    addr='서울시 강남구 도곡동'
    
    #행동양식=>method로 기술한다. 메소드에는 self 인자가 반드시 들어가야 한다
    def info(self):
        print(f'''{self.owner}의 집----
        방 수 : {self.room} 개
        주 소 : {self.addr}
        ''')

    def existAt(self, bunji):
        print('-'*30)
        self.info() #집 정보
        print('세부 주소: ', str(bunji)+"번지에 위치합니다")

if __name__ =='__main__':
    #객체 생성
    #변수명=클래스명() =>객체를 생성
    '''
    객체명.변수 ===> 인스턴스 변수
    객체명.메소드()==> 인스턴스 메소드
    '''
    h1=House() #instance
    h1.info()

    h2=House()
    h2.info()

    h2.owner='홍길동'
    h2.room=3
    h2.addr='마포구 상암동'
    h2.info()

    h1.info()

    h3=House()
    h3.owner='최빛나'
    h3.room=5
    h3.addr='경기도 수원'
    h3.info()

    h1.existAt(100)
    h2.existAt(200)
    h3.existAt(300)