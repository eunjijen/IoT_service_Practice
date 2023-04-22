class Person:
    def __init__(self, name, tel):
        self._name=name
        self._tel=tel

    def showInfo(self):
        return f'''
        이 름 : {self._name}
        연락처 : {self._tel}'''

    def inputInfo(self):
        self._name=input('이름을 입력: ')
        self._tel=input('연락처 입력: ')

if __name__ =='__main__':
    p=Person("아무개","1111000")
    p.inputInfo()
    info=p.showInfo()
    print(info)