# ex58SelectMemo.py
print('--memo테이블에서 select해서 가져와 출력하기----')
config={
    'host':'localhost',
    'user':'scott',
    'password':'tiger',
    'database':'multidb',
    'port':3306,
    'charset':'utf8'
}
import pymysql as mydb

def selectMemoAll():
    try:
        with mydb.connect(**config) as con:
            with con.cursor() as cursor:
                sql='select idx, name, msg, wdate from memo order by idx desc';
                cursor.execute(sql)
                rows=cursor.fetchall() #결과물 가져옥
                mlist=[]
                for row in rows:
                    print(row)
                    s=f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}'
                    mlist.append(s)
                return mlist
    except Exception as ex:
        print('selectMemoAll() DB Error: ', ex)
        return None

if __name__ =='__main__':
    arr=selectMemoAll()
    for s in arr:
        print(s)