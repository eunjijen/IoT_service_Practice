from pymongo import MongoClient
import time

client=MongoClient('mongodb://localhost:27017')
db=client['mydb']

dno=int(input('등록할 부서번호: '))
dname=input('등록할 부서명: ')
loc=input('등록할 부서의 위치: ')

dept_data={
    'deptno':dno,
    'dname':dname,
    'loc':loc
}
result=db.dept.insert_one(dept_data)
print(dname,'부서정보 등록 완료===')

time.sleep(1) #1초 동안 기다림

#모든 부서 정보 가져와서 출력하기
print('#'*50)
cr=db.dept.find()
for r in cr:
    print(r['deptno'],r['dname'],r['loc'])
print('#'*50)
print('전체 document개수: ', db['dept'].estimated_document_count())