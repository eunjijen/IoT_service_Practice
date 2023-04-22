# ex61UpdateMemo.py
print('---memo글 수정하기-----')
import pymysql as mydb
config={
    'host':'localhost',
    'user':'scott',
    'password':'tiger',
    'database':'multidb',
    'port':3306,
    'charset':'utf8'
}
def updateMemo(no=None):
    # 수정할 글 번호 입력받기
    # 수정할 작성자명 입력
    # 수정할 메모내용 입력
    # update문 작성해서 실행
    if no == None:
        return '삭제할 글 번호를 입력해야 해요'
    con = mydb.connect(**config)

    with con:
        with con.cursor() as cr:
            sql = f"select count(idx) from memo where idx = {no}"
            cr.execute(sql)
            row = cr.fetchone()
            if row[0]>0:
                name=input('수정할 작성자명: ')
                msg=input('수정할 메모내용: ')
                # sql=f'update memo set name=\'{name}\', msg=\'{msg}\' where idx={no}'
                # cr.execute(sql)
                sql="update memo set name=%s, msg=%s where idx=%s"
                values=(f"{name}", f"{msg}", no)
                cr.execute(sql, values)

                con.commit()
                return f"내용을 변경했어요"
            else:
                return f"{no}번 글은 없습니다."


no =int(input('수정할 글 번호 입력: '))
result=updateMemo(no)
print(result)