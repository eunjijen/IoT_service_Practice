-- day02 select.sql

USE schooldb;

SHOW TABLES;

SELECT * FROM dept;
SELECT * FROM emp;
SELECT * FROM salgrade;

-- emp에서 사번, 사원명, 급여를 가져와 보여주세요
SELECT empno, ename, sal FROM emp;

-- 산술 표현식
SELECT ename, sal, sal + 300 FROM emp;

-- emp에서 사번, 사원명, 월급여(sal), 보너스(comm), 연봉을 계산해서 출력하세요
-- 연봉 = 월급여 * 12 + 보너스

SELECT empno, ename, sal, comm, sal*12+comm, 
sal*12+ ifnull(comm,0) AS yearSal, job FROM emp;

-- null값과 연산을 하면 모두 null이 된다
-- IFNULL(컬럼명, 대체값): 컬럼값이 null 대체값으로 대체

-- emp에서 사원들의 담당 업무(job)를 가져와 보여주세요
SELECT ename, job FROM emp;

-- 사원들의 업무종류를 출력하사ㅔ요
SELECT distinct job FROM emp;

/*
distinct : 중복행을 제거하여 한번만 출력되도록 한다
			distinct 뒤에 나오는 컬럼들은 모두 영향을 받는다.
			여러개의 컬럼이 기술되면 컬럼의 조합들이 중복되지 않게 나타난다
*/

DESC emp;  -- 칼럼종류

-- [1]  부서별(deptno)로 담당하는 업무를 한번씩 출력하세요.
-- asc: 오름파순, desc: 내림차순
SELECT DISTINCT deptno, job FROM emp ORDER BY deptno ASC;  
-- 부서번호 오름차순으로 정렬 (오름차순이 default)

-- [2] EMP테이블에서 중복되지 않는 부서번호를 출력하세요.
SELECT DISTINCT deptno FROM emp;

-- 데이터 제한과 정렬
/*
SELECT 컬럼들 FROM 테이블명
WHERE 조건절
ORDER BY 정렬할 컬럼명 asc|desc
*/

-- 급여가 3000 이상인 사원의 사번, 이름, 업무, 급여를 출력
SELECT empno, ename, job, sal FROM emp WHERE sal >= 3000
ORDER BY sal desc;


-- EMP테이블에서 담당업무가 MANAGER인 사원의
--	정보를 사원번호,이름,업무,급여,부서번호로 출력하세요.
SELECT empno, ename, job, sal, deptno FROM emp
WHERE job = 'manager';

-- EMP테이블에서 입사일이(hiredate) 1982년 1월1일 이후에 입사한 사원의 
--	사원번호,성명,업무,급여,입사일자를 출력하세요.
SELECT empno, ename, job, sal, hiredate FROM emp
WHERE hiredate > '1982-01-01' ORDER BY hiredate;


-- emp에서 급여가 1300~1500 사이인 사원의 이름, 업무, 급여, 부서번호 출력하세요.
SELECT ename, job, sal, deptno FROM emp
WHERE 1300 <= sal and sal <= 1500;

-- BETWEEN A snd B: A와 B 사이에 있는 [주의] A가 작은값, B가큰값이 와야함
SELECT ename, job, sal, deptno FROM emp
WHERE sal BETWEEN 1300 AND 1500;


-- emp테이블에서 사원번호가 7902,7788,7566인 사원의 사원번호,
-- 이름,업무,급여,입사일자를 출력하세요.
-- 여기서는 =가 값이 같은 것을 의미, 대입연산자 아님
SELECT empno, ename, job, sal,hiredate FROM emp
WHERE empno = '7902' or empno ='7788' or empno ='7566';

-- 컬럼명 in (리스트)
SELECT empno, ename, job, sal, hiredate FROM emp
WHERE empno IN (7902, 7788, 7566);


-- 10번 부서가 아닌 사원의 이름,업무,부서번호를 출력하세요
-- !=, <>  2개 다 not
SELECT ename, job, deptno FROM emp
WHERE deptno != 10 ORDER BY deptno;

SELECT ename, job, deptno FROM emp
WHERE deptno <> 10 ORDER BY deptno;

-- 컬럼명이 길면 select 한 컬럼에 순서에 숫자를 쓸수 있음
-- ename이 1, job가 2... 이렇게
SELECT ename, job, deptno FROM emp
WHERE deptno <> 10 ORDER BY 3 desc;


-- [문제]
-- 	emp테이블에서 업무가 SALESMAN 이거나 PRESIDENT인
-- 	사원의 사원번호,이름,업무,급여를 출력하세요.
SELECT empno, ename, job, sal FROM emp
WHERE job IN ('salesman', 'president');

-- 커미션(COMM)이 300이거나 500이거나 1400인 사원정보를 출력하세요
SELECT * FROM emp
WHERE comm IN (300, 500, 1400);
-- WHERE comm = 300 OR comm = 500 OR comm = 1400;

-- LIKE 연산자      
-- where 컬럼명 like '조건'
-- where 컬럼명 like '%조건'  (앞에 뭐가오든 조건으로 끝나는)  % 는 와일드카드 
-- where 컬럼명 like '조건%'   (뒤에 뭐가 오든 조건으로 시작하는)
-- where 컬럼명 like '%조건%'  

-- emp에서 이름이 s로 시작하는 사원정보를 보여주세요 
SELECT * FROM emp
WHERE ename like 's%';

-- s로 끝나는 사원정보 
SELECT * FROM emp
WHERE ename LIKE '%s';

-- s자가 들어간 사원정보 
SELECT * FROM emp
WHERE ename LIKE '%s%';

-- EMP테이블에서 입사일자가 82년도에 입사한 사원의 사번,이름,업무 
-- 입사일자를 출력하세요.
SELECT empno, ename, job, hiredate FROM emp
WHERE hiredate like '1982%';

SELECT empno, ename, job, hiredate FROM emp
WHERE DATE_FORMAT(hiredate, '%y') LIKE '82';

-- %y면 년도를 2자리로 표현 80, 91... %Y 대문자면 1980으로 표현
SELECT DATE_FORMAT(hiredate, '%y'), DATE_FORMAT(hiredate,'%Y') FROM emp;

/*
%Y, %y : 년도 정보
%m : 월 정보 
%d : 일 정보 
%H : 시간 정보 (24시간 기준)
%h : 시간 정보 (12시간 기준)
%i : 분 정보
%s : 초 정보
%p : AM/PM
*/

SELECT NOW();  -- 시스템의 현재 날짜와 시간 정보를 반환
-- 현재 년월일만 출력
SELECT NOW(), DATE_FORMAT(NOW(), '%Y-%m-%d'), DATE_FORMAT(NOW(),'%y-%m-%d');
-- 현재 시간정보 시분초 출력
SELECT NOW(), DATE_FORMAT(NOW(), '%h:&i:%s %p');

SELECT CURTIME();  -- 시간정보를 반환
SELECT CURTIME(), TIME_FORMAT(CURTIME(), '%H:%i:%s %p');

-- 이름 두번째에 O자가 들어가는 사원정보 보여주세요
-- '_'는 하나의 문자와 매칭된다
SELECT ename FROM emp
WHERE ename LIKE '_o%';  -- 첫번째 글자는 뭐 올거고 2번째에 o가 올거야

-- emp에서 comm이 널인 사원의 사번,이름,커미션을 가져와 출력하세요
-- [주의] null값을 비교할 때는 =로 배교하면 데이터를 가져오지 못한다
-- null값의 비교는 is null / is not null 연산자를 사용

SELECT empno, ename, comm FROM emp
WHERE comm IS not NULL;

SELECT empno, ename, comm FROM emp
WHERE comm is NULL;

-- AND : 양쪽 조건이 TRUE이면 TRUE를 반환
-- OR  : 하나라도 TRUE이면 TRUE를 반환
-- NOT : FALSE이면 TRUE, TRUE면 FALSE로
-- IN :
-- NOT IN :
-- BETWEEN A and B :
-- NOT BETWEEN a AND b :

-- 연산자 우선순위
-- 비교연산자 > NOT > AND > OR


-- EMP테이블에서 급여가 1100이상이고 JOB이 MANAGER인 사원의
-- 사번,이름,업무,급여를 출력하세요.
SELECT empno, ename, job, sal FROM emp
WHERE sal >= 1100 AND job = 'manager' ORDER BY 1;

-- EMP테이블에서 급여가 1100이상이거나 JOB이 MANAGER인 사원의
-- 사번,이름,업무,급여를 출력하세요.
SELECT empno, ename, job, sal FROM emp
WHERE sal >= 1100 or job = 'manager';

-- EMP테이블에서 JOB이 MANAGER,CLERK,ANALYST가 아닌
-- 	 사원의 사번,이름,업무,급여를 출력하세요.
SELECT empno, ename, job, sal FROM emp
WHERE job NOT IN ('manager','clerk','analyst') ORDER BY 1;


-- EMP테이블에서 급여가 1000이상 1500이하가 아닌 사원의 모든 정보를 출력하세요
SELECT * FROM emp
WHERE sal NOT BETWEEN 1000 AND 1500 ORDER BY empno;
  
--  EMP테이블에서 이름에 'S'자가 들어가지 않은 사람의 이름을 모두
-- 출력하세요.
SELECT ename FROM emp
WHERE ename NOT like '%s%';

-- 사원테이블에서 업무가 PRESIDENT이고 급여가 1500이상이거나
-- 업무가 SALESMAN인 사원의 사번,이름,업무,급여를 출력하세요.
SELECT empno, ename, job, sal FROM emp
WHERE job = 'president' AND sal >= 1500 OR job = 'salesman';

-- 어순 : WGHOL 순서 
-- where / group by / having / order by / limit

-- ORDER BY 절
-- ASC: 오름차순
-- DESC: 내림차순
-- NULL 값: 오름차순에서는 제일 뒤에, 내림차순일 때는 제일 앞에 온다


-- 사원 테이블에서 부서번호로 정렬한 후 부서번호가 같을 경우
-- 급여가 많은 순으로 정렬하여 사번,이름,업무,부서번호,급여를 출력하세요.
SELECT empno, ename, job, deptno, sal FROM emp
order BY deptno, sal desc;

-- 사원 테이블에서 첫번째 정렬은 부서번호로, 두번째 정렬은
-- 업무로, 세번째 정렬은 급여가 많은 순으로 정렬하여
-- 사번,이름,입사일자,부서번호,업무,급여를 출력하세요.
SELECT empno, ename, hiredate, deptno, job, sal FROM emp
ORDER BY deptno, job, sal DESC;

SELECT ename, job, sal, sal*12 AS annsal FROM emp
ORDER BY sal*12 ASC;

SELECT ename, sal, sal*12 FROM emp
ORDER BY 1;

SELECT ename, sal, sal*12 FROM emp
ORDER BY 3 DESC;

-- 사원 중 급여가 가장 높은 순으로 TOP 3안에 드는 사원정보를 보여주세요
-- limit
-- offset
SELECT empno, ename, sal, job FROM emp
ORDER BY sal DESC LIMIT 3; -- offset 0;

SELECT empno, ename, sal, job FROM emp
ORDER BY sal DESC LIMIT 3 OFFSET 6;


-- 사원테이블이서 입사일이 1981 2월20일 ~ 1981 5월1일 사이에
--	   입사한 사원의 이름,업무 입사일을 출력하되, 입사일 순으로 출력하세요.
SELECT ename, job, hiredate FROM emp
WHERE hiredate BETWEEN '1981-02-20' AND '1981-05-01'
ORDER BY hiredate DESC;

--  사원테이블에서 보너스가 급여보다 10%만큼  많은 
-- 사원의 이름,급여,보너스를 출력하세요.
SELECT ename, sal, comm FROM emp
WHERE comm >= sal * 1.1;

-- 사원테이블에서 이름에 L이 두자가 있고 부서가 30이거나
--	  또는 관리자가 7782번인 사원의 정보를 출력하세요.
SELECT * FROM emp 
WHERE ename LIKE "%LL%" and deptno = '30' OR mgr = '7782';




