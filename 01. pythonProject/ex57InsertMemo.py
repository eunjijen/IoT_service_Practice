# ex57InsertMemo.py
print('---scott 계정 multidb의 Memo테이블 insert--------')
config={
    'host':'localhost',
    'user':'scott',
    'password':'tiger',
    'database':'multidb',
    'port':3306,
    'charset':'utf8'
}
import pymysql as mydb

def insertMemo1():
    with mydb.connect(**config) as con:
        cursor=con.cursor()
        name='이미나'
        msg='파이썬에서 처음으로 글을 씁니다'

        sql=f'''insert into memo(name,msg) values('{name}','{msg}')'''
        print(sql)
        cursor.execute(sql)

        print('메모글 등록 완료!!')
        cursor.close()
        con.commit() #트랜잭션 완료 ==>commit을 해야 실제 DB에 저장된다

def insertMemo2():
    name=input('작성자를 입력: ')
    msg=input('메모 내용을 입력: ')

    with mydb.connect(**config) as con:
        with con.cursor() as cursor:
            # sql=f"insert into memo(name,msg) values('{name}','{msg}')"
            sql="insert into memo(name,msg) values(%s,%s)"
            print(sql)
            values=(f'{name}',f'{msg}')
            cursor.execute(sql,values)
            con.commit()
            # cursor.execute(sql %(name,msg))
            print(f'{name}님의 글을 등록했습니다')

if __name__ =='__main__':
    # insertMemo1()
    insertMemo2()
