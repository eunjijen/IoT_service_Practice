from school.Person import Person
'''
패키지명.모듈명 import 클래스명
'''
class Student(Person):
    def __init__(self,id=0,name=None,tel=None,cname=None):
        self._id=id
        self._name=name
        self._tel=tel
        self._cname=cname

    def inputInfo(self):
        self._id=input('학번을 입력: ')
        #이름, 연락처
        super().inputInfo()
        self._cname=input('학급명을 입력: ')

    def showInfo(self):
        return f'''
        학  번: {self._id}{super().showInfo()}  
        학급명: {self._cname}
        '''

if __name__ =='__main__':
    s=Student(1,"최철수","2323","IOT반")
    s.inputInfo()
    print(s.showInfo())