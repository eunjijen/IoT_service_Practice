# ex56CreateMemo.py
print('--scott계정의 multidb사용-----')
'''
한줄 메모장: Memo테이블을 생성하는 문장을 작성한 뒤
파이썬에서 실행시키세요
테이블명: Memo
    - 글번호 (idx): int PK 자동증가
    - 작성자 (name): varchar(20)
    - 메모내용(msg):  varchar(200)
    - 작성일 (wdate): date 디폴트값 현재날짜
'''
import pymysql as mydb
con= mydb.connect(host='localhost', user='scott', password='tiger', db='multidb',charset='utf8')
cursor=con.cursor()
sql='''create table if not exists Memo
        (idx int auto_increment primary key ,
        name varchar(20),
        msg varchar(200),
        wdate date default curdate()
        )
    '''
cursor.execute(sql)
print('테이블 생성 성공!!')
cursor.close()
con.close()