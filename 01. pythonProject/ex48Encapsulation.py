# ex48Encapsulation.py
print('---캡슐화----')
'''
객체지향 언어의 특징 (파이썬,자바,C++)
 [1] 추상화 ===> 객체를 프로그램 세계로 끌어들이는 것. class로 구성하는 것
 [2] 캡슐화 ===> 데이터를 감추는 기법
            다른 클래스에서 데이터를 함부로 변경하거나 꺼내쓸 수 없도록 접근을 제약하는 것을 캡슐화라고 한다
 [3] 상속성
 [4] 다형성
'''
'''
mypkg의 myModule1에 있는 Dog객체를 생성하고
sound,이름,나이,품종을 출력하세요
'''
from mypkg.myModule1 import Dog
print('-'*30)
print(Dog.sound)
d1=Dog("쫑이",5,"Mix")
print('d1.name: ',d1.name)
print('d1.age: ', d1.age)
# print('d1.__breed: ',d1.__breed) [x]
#AttributeError: 'Dog' object has no attribute '__breed'
print('d1.getBreed(): ', d1.getBreed())

d1.setBreed("푸들")
print('d1.getBreed(): ', d1.getBreed())
'''
# 자료와 알고리즘이 구현된 함수를 하나로 묶고 공용 인터페이스만 으로 접근을 제한하여 객체의 세부
# 내용을 외부로 부터 감추는 기법을 캡슐화(encapsulation)라고 한다. 클래스에서 은닉정보는 변수 앞
# 부분에 _기호를 연속하여 두 개 넣으면 외부에서 접근이 불가능한 은닉(private)변수가 된다
그리고
# 은닉 변수를 외부에서 접근할 수 있는 공용 인터페이스는 getter와 setter로 분류한다. 
# getter는 외부에서 은닉된 값을 꺼내오는 메서드이고, setter는 외부에서 값을 수정하는 메서드이다
[1] 생성자함수 구성
[2] setter, getter구성하기
[3] 계좌정보를 문자열로 반환하는 메서드 구성하기
[4] 객체 생성해서 메서드 호출하기
private : __name  자기클래스 내에서만 접근 가능. 외부에서는 접근 불가
protected: _name  부모 자식의 상속관계를 맺을 때 자식에서 부모로부터 상속받은 변수는 접근 가능
public : name 어디서든 접근 가능
'''
