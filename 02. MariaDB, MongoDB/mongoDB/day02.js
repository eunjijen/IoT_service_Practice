use mydb
//collection : table과 같
show collections

db.createCollection('member',{capped:true, size:10000})

db.member.find()
/* CRUD
 Create: insertOne() : 1개의 document를 삽입
         insertMany(): 여러 개의 document를 삽입
 Read : findOne() : 매칭되는 한 개의 document를 조회한다
        find() : 매칭되는 여러 document의 list를 조회함
        find({조건},{필드들})
*/
db.member.insertOne({name:'홍길동',userid:'hong', tel:'010-1111', age:20})
//조회
db.member.find({})
db.getCollection('member').find()

db.member.insertMany([
{name:'김철수',userid:'kim',tel:'010-2222',age:22, grade:'A'},
{name:'신철민',userid:'shin',tel:'010-3222',age:25, grade:'C'},
{name:'김유신',userid:'youshin',tel:'010-4222',age:28, grade:'B'},
{name:'이철수',userid:'lee',tel:'010-5222',age:32, grade:'D'},
{name:'임승환',userid:'lim',tel:'010-6222',age:19, grade:'B'}])

db.member.find()
//select _id,name,userid from member
db.member.find({},{name:true,userid:true})

db.member.find({},{_id:false,name:true, userid:true})
//false:0, true:1
db.member.find({},{_id:0,name:1,tel:1})

//select * from member where age=20
db.member.find({age:20},{})

//select * from member where age=20 and userid='hong'
db.member.find({age:20,userid:'hong'},{})

//select * from member where age=19 or userid='hong'
db.member.find({$or:[{age:19},{userid:'hong'}]})

db.member.find({$nor:[{age:19},{userid:'hong'}]})
/*
논리연산
$and : 배열안 두개 이상의 조건이 모두 참인 경우를 반환 
$or  : 배열안 두개 이상의 조건 중 하나라도 참인 경우를 반환 
$nor : $or의 반대. 배열안 두개 이상의 조건이 모두 아닌 경우 를 반환

비교 문법
$eq     =    
$gt     >    
$gte    >=   
$in          목록 중의 어느 하나라도 있는지 여부를 체크
$lt     <    
$lte    <=   
$ne     !=   not equal
$nin         $in의 반대. not in
*/

//select * from member where age>20
db.member.find({age:{$gt:20}})

//select * from member where age>=20
db.member.find({age:{$gte:20}})

//<1> userid가 shin 인 document의 name, userid, tel을 가져오기
db.member.find({userid:'shin'},{name:1,userid:1,tel:1})

//<2> age가 25세 이거나 이름이 김유신인 회원의 모든 정보 가져오기
db.member.find({$or:[{age:25},{name:'김유신'}]})
//<3> 나이가 22세 미만인 회원의 이름,나이만 가져오기
db.member.find({age:{$lt:22}},{name:1,age:1})

//<4> emp에서 사원의 이름과 급여를 가져와 보여주세요
db.emp.find({},{ename:1,sal:1,_id:0})
//<5> emp에서 담당 업무가 'MANAGER'인 사원의 사번,이름,업무를 보여주세요
db.emp.find({job:'MANAGER'},{empno:1,ename:1,job:1})

//<6> emp에서 급여가 3000 이상인 사원의 사원번호,이름,	담당업무,급여를 출력하세요
db.emp.find({sal:{$gte:3000}},{empno:1,ename:1,job:1,sal:1})

/*<7> emp에서 급여가 1300에서 2000사이의 사원의 이름,업무,급여,
	부서번호를 출력하세요*/
db.emp.find({$and:[{sal:{$gte:1300}},{sal:{$lte:2000}}]},{ename:1,job:1,sal:1,deptno:1})

//<8>	emp에서 사원번호가 7369,7654,7934인 사원의 사원번호,
//	이름,업무,급여,입사일자를 출력하세요.
db.emp.find({empno:{$in:[7369,7654,7934]}},{empno:1,ename:1,job:1,sal:1,hiredate:1})
//<9>	emp에서 부서번호가 20번 부서인 사원의 이름,업무,부서번호를 출력하세요
db.emp.find({deptno:20},{ename:1,job:1,deptno:1})
//<10> emp에서	부서번호가 20번 부서가 아닌 사원의 이름,업무,부서번호를 출력하세요
db.emp.find({deptno:{$ne:20}},{ename:1,job:1,deptno:1})
//<11> emp에서 업무가 CLERK이거나 MANAGER인 사원의 모든 정보를 출력하세요
db.emp.find({$or:[{job:'CLERK'},{job:'MANAGER'}]})
db.emp.find({job:{$in:['CLERK','MANAGER']}})
//<12> emp에서 업무가 CLERK이거나 MANAGER가 아닌 사원의 모든 정보를 출력하세요
db.emp.find({$nor:[{job:'CLERK'},{job:'MANAGER'}]})
db.emp.find({job:{$nin:['CLERK','MANAGER']}})

//like절 ( where name like '%길동%) ==> 정규식
//$regex
//select * from member where userid like '%o%'
db.member.find({userid:{$regex:/o/}})
db.member.find({userid:/sh/})
//userid 가 sh로 시작하는 회원정보를 보여주세요
//정규식에서 사용하는 메타문자 : /^sh/(시작: ^)
//                        /sh$/ (종료: $)
//select * from member where userid like 'sh%'
db.member.find({userid:/^sh/})

//select * from member where userid like '%ng'
db.member.find({userid:/ng$/})

/*[실습]------------------------------
<1> emp에서 이름이 S로 시작하는 사람의 정보를 보여주세요
<2>이름 중 S로 끝나는 사람의 정보를 보여주세요
<3>이름 중 E자가 들어가는 사람의 정보를 보여주세요.
----------------------------------------*/
db.emp.find({ename:{$regex:/^S/}})

db.emp.find({ename:{$regex:/S$/}})

db.emp.find({ename:{$regex:/E/}})

//[order by절] : sort({})함수 활용.
db.member.find({age:{$lte:22}}).sort({age:1}) //order by age asc

db.member.find({age:{$lte:22}}).sort({age:-1}) //order by age desc

//[실습]
//<1>member에서 회원의 나이를 내림차순으로 정렬하고, 
//  같은 나이일 때는 이름 가나다순으로 정렬해서 출력하세요
db.member.find().sort({age:-1, name:1})
//<2> employees에서 부서번호로 정렬한 후 부서번호가 같을 경우
//	급여가 많은 순으로 정렬하여 사번,이름,부서번호,급여를 출력하세요
db.emp.find({},{empno:1,ename:1,deptno:1,sal:1}).sort({deptno:1,sal:-1})

//<3> employees에서 부서번호가 10,20인 사원의 이름,부서번호,업무를 출력하되
//    이름 순으로 정렬하시오
db.emp.find({deptno:{$in:[10,20]}},{ename:1,deptno:1,job:1}).sort({ename:1})

//select count(*) from member
//[count()]함수 활용
db.member.find().count()

//select count(*) from member where age>22
db.member.find({age:{$gt:22}}).count()

//limit(n)
db.member.find().sort({age:-1}).limit(3)









