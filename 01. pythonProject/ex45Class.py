print('--인스턴스 변수, 클래스 변수----')
'''멤버변수
[1] 클래스 변수 : 해당 클래스 내에서 선언된 변수. 모든 인스턴스가 값을 공유하는 변수 "클래스명.변수" 식으로 접근한다
[2] 인스턴스 변수: __init__() 메소드 내에서 선언된 변수로  ====>"객체명.변수"
                인스턴스가 생성될 때마다 새로운 값이 할당된다.
'''
class Dog:
    sound="멍 멍 ~~" #self로 참조되지 않는 멤버변수를 클래스 변수라고 한다
    color='@@'
    def __init__(self, name="강아지", age=1, breed=None):
        self.name=name #인스턴스 변수
        self.age=age
        self.breed=breed
        self.color='white' #인스턴스 변수
    def show(self):
        s=f'''
        이 름: {self.name}
        나 이: {self.age}
        종 류: {self.breed}
        '''
        return s

'''
강아지 객체 2마리 생성하고 
show()호출해보기
'''
d1=Dog()
result=d1.show()
print(result)

d2=Dog("쫑이",2,"진돗개")
print(d2.show())
print('강아지 우는 소리~~~~')
print(Dog.sound)
print(Dog.color)
print(d1.color, d2.color)
# print(Dog.name)
#AttributeError: type object 'Dog' has no attribute 'name'
print(d1.name, d1.age)
print(d2.name, d2.age)
print(Dog.sound, d1.sound, d2.sound)
d1.sound="왈 왈~~"
print('d1.sound: ', d1.sound)
print('d2.sound: ', d2.sound)
print('Dog.sound: ', Dog.sound)


