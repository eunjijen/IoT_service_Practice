from school.Student import Student
from school.Teacher import Teacher

class SchoolApp:
    count=0 #클래스 변수
    arr=[] #등록된 사람들을 저장할 리스트

    def mainMenu(self):
        print('----Menu-------')
        print('1. 등    록')
        print('2. 출    력')
        print('3. 검    색')
        print('4. 삭    제')
        print('9. 종    료')
    def subMenu(self):
        print('---등록 Menu------')
        print('1. 학생 등록')
        print('2. 교사 등록')
        print('3. 직원 등록')
        print('4. 상위 메뉴')
        
    def register(self): #등록하는 로직을 처리하는 메소드
        while True:
            self.subMenu()
            num=int(input('메뉴 번호를 선택하세요: '))
            if num==4:
                # break
                return  #register()메소드를 호출한 쪽으로 돌아간다
            elif num==1: #학생 등록
                p=Student()
                p.inputInfo() 
            elif num==2: #교사 등록
                p=Teacher()
                p.inputInfo()
            elif num==3: #직원 등록
                pass
            else:
                print('메뉴에 없는 번호에요')
                continue
            print(p.showInfo())
            no=int(input('위 정보를 등록할까요? 1. Yes  2.No'))
            if no==1:
                SchoolApp.arr.append(p)
                SchoolApp.count+=1
                print(f'현재 {SchoolApp.count} 명 등록 완료!!')
            elif no==2:
                print('등록을 취소했습니다')

    def printAll(self):
        #arr에 저장된 사람들 정보를 반복문 돌면서 출력
        for p in SchoolApp.arr:
            if type(p)==Student:
                print('---학생 정보---')
            elif type(p)==Teacher:
                print('---교사 정보---')
            print(p.showInfo())

    def find(self):
        name=input('검색할 사람의 이름을 입력: ')
        isExist=False
        for p in SchoolApp.arr:
            if p._name==name:
                isExist=True
                print(p.showInfo())
                break                
        if not isExist: # if isExist==False:
            print(name,'님은 존재하지 않습니다')
            
    def delete(self):
        name = input('삭제할 사람의 이름을 입력: ')
        isExist=False
        for p in SchoolApp.arr:
            if p._name==name:
                isExist=True
                SchoolApp.arr.remove(p)
                break
        if not isExist:
            print(f'{name}님은 존재하지 않아요')
        else:
            print(f'{name}님의 정보를 삭제했습니다')
        
if __name__ =='__main__':
    app=SchoolApp()
    while True:
        app.mainMenu()
        num=int(input('메뉴 번호를 선택하세요: '))
        if num==9:
            print('Bye Bye~')
            exit(0) #시스템 종료 (0: 정상 종료, 음수:에러발생해서 종료시)
        elif num<1 or num >4:
            print('메뉴에 없는 번호에요!!')
            continue
        elif num==1: #등록=> 서브 메뉴 보여주기
            app.register()
        elif num==2: #출력
            app.printAll()
        elif num==3: #검색
            app.find()
        elif num==4: #삭제
            app.delete()



