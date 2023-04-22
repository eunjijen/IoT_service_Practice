# ex59FindMemo.py
print('---memo글 검색하기-----')
'''
-- 검색 메뉴------------
1. 작성자   2. 메모내용
----------------------

1번 선택: 
작성자 이름 입력: 길동
=> 길동이란 이름을 가진 사람이 쓴글만 나오도록

2번 선택
메모 내용의 키워드 입력: 안녕
안녕이 들어간 메모내용 모두 출력하기
'''
import pymysql as mydb
config={
    'host':'localhost',
    'user':'scott',
    'password':'tiger',
    'database':'multidb',
    'port':3306,
    'charset':'utf8'
}
def findMemo(ftype='name',keword=None):
    if keword==None:
        return "검색어를 입력해야 해요"

    with mydb.connect(**config) as con:
        with con.cursor() as cr:
            if ftype=='name':
                sql=f"select idx, name, msg, wdate from memo where name like '%{keword}%' order by 1 desc";
            elif ftype=='msg':
                sql=f"select idx, name, msg, wdate from memo where msg like '%{keword}%' order by 1 desc"
            print(sql)
            cr.execute(sql)
            rows=cr.fetchall()
            print('rows type: ', type(rows), rows)
            if len(rows)==0:
                print(keword,'데이터는 없습니다')
                return None
            else:
                lst=[]
                for r in rows:
                    s=f'{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}'
                    lst.append(s)
                return lst

if __name__ =='__main__':
    print(''' ---검색 메뉴-----
                1. 작성자로 검색
                2. 메모 내용으로 검색
              ----------------''')
    num=int(input('입력하세요: '))

    if num==1:
        ftype='name'
        keyword=input('검색할 작성자명을 입력하세요: ')
    elif num==2:
        ftype='msg'
        keyword=input('검색할 내용의 키워드를 입력하세요: ')

    arr=findMemo(ftype, keyword)

    print('#'*30)
    print(f'Idx\tName\tMsg\tWdate')
    print('#' * 30)
    if arr != None and len(arr)>0:
        for memo in arr:
            print(memo)