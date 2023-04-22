#50Inheritance.py
print('---상속성------')
'''
Inheritance

        Animal (부모클래스)
        sound
        age
        cry()
        
Cat         Dog         Duck(자식클래스)
name        name        name
info()      info()      info()

부모클래스에 공통적인 변수나 메소드를 정의하고,
자식클래스에서 부모클래스를 상속받아 자기것 처럼
사용하도록 하는 것=> 상속성

class 부모:  #디폴트로 object클래스를 묵시적으로 상속 받는다
    pass

class 자식(부모):  <==부모를 상속받는다
    pass
'''
class Parent:
    def __init__(self,name, age):
        self.__name=name
        self.__age=age

    def showInfo(self):
        # print('이 름: %s, 나이: %d'  %(self.__name, self.__age) )
        print('이 름: %s\n나이: %d'  %(self.getName(), self.getAge()) )
    #setter
    def setName(self, name):
        self.__name=name
    def setAge(self, age):
        self.__age=age
    #getter
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

class Child(Parent):
    def __init__(self,name,age,hobby):
        #self.__name=name #[x]
        #self.__age=age   #[x]
        self.setName(name)
        self.setAge(age)
        self.__hobby=hobby
    #부모의 메소드를 재정의-메소드 오버라이드(재정의) : 부모로부터 상속받은 메소드를 자식이 다시 정의하는 것
    def showInfo(self):
        # print('Name: %s Age:%d Hobby:%s' %(self.getName(), self.getAge(),self.__hobby))
        super().showInfo() #super() 부모로부터 상속받은 것을 참조할때 super() 이름, 나이 출력
        print("취미: ", self.__hobby)
        
if __name__=='__main__':
    p1=Parent("김부모",44)
    p1.showInfo()

    # Child객체 생성해서 showInfo()호출해보기
    c1=Child("김철이",20,"축구")
    c1.showInfo()
    
    '''
    부모, 자식 객체 1개씨 더 생성한 뒤
    list에 p1,c1, 부모,자식 들을 저장하세요
    
    반복문 이용해서 list에 저장된 객체들의 정보 출력하기
    '''
    p2 = Parent('이부모', 50)
    c2 = Child('이자식', 23, '파이썬')

    print('-' * 10)
    list1 = [p1, p2, c1, c2]

    for i in list1:
        print('-' * 10)
        i.showInfo()






