print('--인스턴스 메소드, 클래스 메소드----')
'''
메소드 종류
- 인스턴스 메소드: self 키워드를 사용. 객체명.메소드명()
- 클래스 메소드 : cls 키워드를 사용한다. 클래스명.메소드명()
                메소드 앞에 '@classmethod' 함수 장식자를 붙여 사용해야 함
                @classmethod를 붙이지 않으면 제대로 동작하지 않을 수 있다.
- 정적 메소드 : self,cls를 사용하지 않는다. 따라서 클래스나 인스턴스 영역에서 접근 할 수 없다.
                @staticmethod 로 표기해야 한다.
                정적 메소드는 정적인 상태를 갖는 기능을 만들때 사용한다
                정적 메소드도 '클래스명.메소드명'으로 접근한다
'''
class MyDate:
    content='MyDate 클래스' #클래스 변수
    def __init__(self,yy,mm,dd):
        self.year=yy
        self.month=mm
        self.date=dd
    def display(self, sep='-'): #인스턴스 메서드
        print(f'%d{sep}%d{sep}%d' %(self.year, self.month, self.date))

    @classmethod
    def date_string(cls, dateStr):
        y=dateStr[:4]
        m=dateStr[4:6]
        d=dateStr[6:]
        print(f'{y}년 {m}월 {d}일')
        print(cls.content) #클래스 변수나 클래스 메서드를 접근할때 cls를 이용할 수 있다
        print('---------------')

    @staticmethod
    def print_info():
        print('This is a instanceof MyDate')
'''
[1] content변수 값을 출력하기

[2] display()메소드를 호출하기

[3] date_string('20230206') 호출하기
'''
if __name__=="__main__" :
    print(MyDate.content)

    today=MyDate(23, 2, 6)
    today.display()
    today.display("/")
    # MyDate.display("@") [x]
    today.date_string("20230206") #[o]
    MyDate.date_string("20241225") #[o]

    MyDate.print_info()