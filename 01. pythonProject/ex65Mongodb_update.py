from pymongo import *

client=MongoClient('mongodb://localhost:27017')
db=client['mydb']

empno=int(input('수정할 사원의 사번 입력: '))
dno=int(input('수정할 부서번호 입력: '))
job=input('수정할 담당업무 입력: ')

cr=db.emp.find({'empno':empno})
cnt=0
for r in cr:
    cnt+=1

if cnt <=0:
    print('수정할 사원은 존재하지 않아요')
elif cnt==1:
    result=db.emp.update_one({'empno':empno},{'$set':{'deptno':dno,'job':job}})
    print(result.modified_count,'문서가 수정되었어요')
else:
    print(cnt,'명 있어요')
import time
time.sleep(1) #1초간 쉬기
cr=db.emp.find({'empno':empno})
print('##수정 결과###################')
for r in cr:
    print(r)
print('@'*50)

name=input('수정할 사원의 이름 키워드 입력: ')
filter={'ename':{'$regex':name.upper()}}
values={'$set':{'deptno':dno,'job':job.upper()}}

result=db.emp.update_many(filter, values)
print(result.modified_count,'개의 문서가 수정되었습니다')






