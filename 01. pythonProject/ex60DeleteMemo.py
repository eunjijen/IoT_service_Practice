# ex60DeleteMemo.py
print('--글 삭제------')
import pymysql as mydb
config={
    'host':'localhost',
    'user':'scott',
    'password':'tiger',
    'database':'multidb',
    'port':3306,
    'charset':'utf8'
}

def deleteMemo(no=None):
    if no==None:
        return "삭제할 글 번호를 입력해야 해요"
    try:
        con=mydb.connect(**config)
        with con:
            with con.cursor() as cr:
                sql=f"select count(idx) from memo where idx={no}"
                cr.execute(sql)
                row=cr.fetchone() #결과 테이블이 단일행일 경우는 fetchone()으로 가져온다
                print('row=',row, type(row))
                if row[0]>0:
                    sql=f'delete from memo where idx={no}'
                    cr.execute(sql)
                    con.commit()
                    return f"{no}번 글을 삭제했습니다"
                else:
                    return f"{no}번 글은 없습니다"
    except Exception as ex:
        print('DB Error: ', ex)
        con.rollback()
        return f"{no}번 글을 삭제하는 중 에러 발생했어요"

no=int(input('삭제할 글 번호 입력: '))
result=deleteMemo(no)
print(result)


