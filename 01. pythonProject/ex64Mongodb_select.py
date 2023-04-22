from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')
db=client['mydb']
print(client.list_database_names())
print()
#emp에서 10번 부서 사원정보를 보여주세요
cr=db['emp'].find({'deptno':10})

for r in cr:
    print(r['empno'],r['ename'],r['deptno'],r['sal'], r['hiredate'])
print('#'*50)
# 급여가 3000 이상인 사원의 ename, sal,job 만 가져와서 보여주세요
cr=db.emp.find({'sal':{'$gte':3000}},{'_id':0,'ename':1,'sal':1,'job':1})
for r in cr:
    print(r['ename'], end='\t')
    print(r['sal'], end='\t')
    print(r['job'], end='\n')
print('*'*50)
# 10,30번 부서이면서 급여가 3000미만인 사원정보를 보여주셍
cr=db.emp.find({'$and':[{'deptno':{'$in':[10,30]}},{'sal':{'$lt':3000}}]}).limit(2)
for r in cr:
    print(r)
print('-'*50)

name=input('검색할 사원 이름을 입력: ')
cr=db.emp.find({'ename':name.upper()}) #upper(): 대문자로 변경, lower(): 소문자로
for r in cr:
    print(r['ename'], r['job'], r['sal'])
print('#'*50)

name=input('검색할 사원명 입력 like 검색: ')
cr=db.emp.find({'ename':{'$regex':name.upper()}})
cnt=0
for r in cr:
    print(r['ename'], r['job'])
    cnt+=1
if cnt==0:
    print('like검색 결과 없습니다')
print('*'*50)