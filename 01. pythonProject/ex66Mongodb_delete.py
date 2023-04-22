from pymongo import *
import time
try:
    client=MongoClient('mongodb://localhost:27017')
    db=client['mydb']
    print(client.list_database_names())
    print('#'*50)
    #삭제전 모든 문서 보여주기
    cr=db.emp.find()
    for r in cr:
        print(r)
    print('#' * 50)
    
    name=input('삭제할 사원의 이름을 입력하세요: ')
    result=db.emp.delete_many({'ename':name.upper()})
    # delete_one({}) : 1개의 document 삭제
    print(result.deleted_count,'명 삭제했습니다')
    time.sleep(1)
    cr=db.emp.find()
    print('**삭제 후 전체 문서*********************')
    for r in cr:
        print(r)

except Exception as ex:
    print('Error: ',ex)