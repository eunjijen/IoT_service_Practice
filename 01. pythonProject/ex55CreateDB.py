# ex55CreateDB.py
print('--Memo테이블 생성하기-----')
import pymysql
#[1]  데이터베이스에 연결
# con=pymysql.connect(host="localhost",user="root", password="1234",db="schooldb",charset="utf8")
con=pymysql.connect(host="localhost",user="scott", password="tiger",db="multidb",charset="utf8")
print('con: ', con)
#[2] 커넥션 통해 cursor객체 얻어오기 
cursor=con.cursor()

#[3] sql문 작성
sql="show tables"

#[4] sql문을 실행: cursor객체의 execute()함수 이용
cursor.execute(sql)

#[5] sql문 실행 결과를 추출 : cursor객체의 fetchall()/fetchone()/fetchmany()
tables=cursor.fetchall()
print('tables: ',tables)

if tables:
    print('table이 있어요')
    for tb in tables:
        print(tb[0])
        print('*'*20)
else:
    print('table이 없어요')
#[6] DB연결 자원 반납 : 커서.close(), 커넥션.close()
cursor.close()
con.close()
