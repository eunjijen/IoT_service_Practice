print('--memo_db.py 모듈--')
class Memo:
    '''
    memo테이블이 가지고 있는 컬럼들을 Memo 클래스의
    멤버변수(instance변수) 로 구성하기
    생성자 구성하기
    '''
    pass

class DataManager:
    '''
        CRUD 기능을 갖는 메소드를 구성
    '''
    def addMemo(self, memo):
        '''
        memo객체를 매개변수로 받아서
        db에 insert문을 실행
        '''


    def listMemo(self):
        '''
        전체 메모글을 가져와서 ==> row(record) 데이터를 memo객체에 담아서
         ==> list에 memo객체들을 append 해서 최종으로 list반환
        '''



if __name__ =='__main__':
    pass
