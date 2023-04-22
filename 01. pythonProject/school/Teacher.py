import school.Person as sc
class Teacher(sc.Person):
    def __init__(self,id=0,name=None,tel=None,subject=None):
        self._id=id
        super().__init__(name,tel)
        self._subject=subject

    def inputInfo(self):
        self._id=input('교번을 입력: ')
        super().inputInfo()
        self._subject=input('과목명을 입력: ')

    def showInfo(self):
        return f'''
        교  번: {self._id}{super().showInfo()}
        과  목: {self._subject}
        '''