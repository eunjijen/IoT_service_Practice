use mydb
db.member.find().limit(1)
db.member.findOne()

// distinct()
db.emp.distinct('deptno')
//<1> employees에서 30번 부서의 사원수를 출력하시오.
db.emp.find({deptno:30}).count()

//<2> employees에서 보너스(comm)을 받는 사원의 수를 출력하시오
//select count(comm) from emp

db.emp.find({comm:{$exists:true}}).count()
db.emp.find({},{ename:1,comm:1})
db.emp.find({comm:{$ne:0}}).count()

//<3> 직업이 SALESMAN이면서 보너스를 100이상 받는 사원수를 출력하시오
db.emp.find({job:'SALESMAN',comm:{$gte:100}}).count()
//<4> employees에서 중복되지 않는 부서번호를 출력하세요.
db.emp.distinct('deptno')
//<5> employees의 직업군을 보여주세요
db.emp.distinct('job')
/* CRUD
Update
    : updateOne()/updateMany()
      replaceOne(): document를 대체  
*/
db.member.find()
db.member.replaceOne({userid:'hong'},
{name:'홍일동',tel:'010-7777',userid:'hong',age:21,grade:'B'},{upsert:true})
//update member set age=21 where userid='hong'
db.member.updateOne({userid:'hong'},{$set:{age:21}})
db.member.find()

//update meber set grade='A' where age <22
//updateManay()
db.member.updateMany({age:{$lt:22}},{$set:{grade:'A'}})


//emp에서 급여가 2000미만이 사원들의 
db.emp.find()
db.emp.updateMany({sal:{$lt:2000}},{$set:{comm:100}})

//emp에서 job이 salesman인 사원들의 comm을 50씩 증가시키세요
db.emp.updateMany({job:'SALESMAN'},{$inc:{comm:50}})

db.emp.find({job:'SALESMAN'})
/*update시 사용하는 연산자
$set : 필드값 설정
$inc : 필드값을 증가시키거나 감소시킴
$mul: 곱한 값으로 수정
$rename: 필드명을 새이름으로 변경한다
$min: 필드의 값이 주어진 값보다 클 경우 새 값으로 교체합니다. 
     만약 원래 값이 200이었고 $min의 값이 150이었다면 150으로 바뀝니다. 
     기존 기록을 경신하는 경우 사용됩니다.
$max: 필드의 값이 주어진 값보다 작을 경우 새 값으로 교체합니다. 
만약 원래 값이 800이었고 $max의 값이 950이라면, 950으로 바뀝니다. 
*/
//update emp set sal=sal*2 where empno=7788
db.emp.update({empno:7788},{$mul:{sal:2}})
db.emp.find({empno:7788})
db.emp.find()
db.emp.updateMany({},{$min:{comm:100}})

//comm이 100보다 큰 사원들의 comm만 100으로 수정됨

//emp사원들의 급여 최대값을 3000으로 맞추세요
//급여가 3000미만인 사원의 급여를 3000으로 수정
db.emp.updateMany({},{$max:{sal:3000}})
db.emp.find()
//alter table emp rename column comm to bonus
db.emp.updateMany({},{$rename:{'comm':'bonus'}})
db.emp.find()

//$currentDate:{필드명:true}
//$currentDate:{필드명:{$type:'timestamp'}}
//$unset : 해당 필드를 제거한다
db.emp.updateMany({},{$currentDate:{indate:true}})
db.emp.updateMany({},{$currentDate:{indate:{$type:'timestamp'}}})

db.emp.updateMany({},{$unset:{indate:''}})
db.emp.find()

/* CRUD
Delete: deleteOne()/ deleteMany()
deleteMany({조건}) : 특정 조건의 document들을 삭제함
deleteMay({}): 모든 document를 삭제함
*/
db.emp.find()

db.emp.deleteMany({})
use mydb
show collections

db.emp.find()

db.emp.drop()

db.dropDatabase()






