-- day06_subquery.sql

-- 사원테이블에서 scott의 급여보다 많은 사원의 사원번호,이름,업무
--	급여를 출력하세요.

SELECT sal FROM emp WHERE ename = 'scott';

SELECT empno, ename, job, sal FROM emp
WHERE sal > 3000;

SELECT empno, ename, job, sal FROM emp
WHERE sal > (SELECT sal FROM emp WHERE ename = 'scott')

-- 1] 사원테이블에서 사원번호가 7521인 사원과 업무가 같고 급여가
-- 7934인 사원보다 많은 사원의 사번,이름,업무,입사일자,급여를 출력하세요

select empno, ename, job, hiredate, sal FROM emp
WHERE job = (select job FROM emp WHERE empno = 7521)
AND sal > (SELECT sal FROM emp WHERE empno = 7934);


-- 단일행 subquery
-- 2]사원테이블에서 급여의 평균보다 적은 사원의 사번,이름,업무,급여,부서번호를 출력하세요.
SELECT empno, ename, job, sal, deptno FROM emp
WHERE sal < (SELECT AVG(sal) FROM emp);

-- 3] 사원테이블에서 사원들의 부서별 최소급여가 30번 부서의 최소급여
-- 보다 많은 부서번호를 출력하세요.
SELECT deptno, MIN(sal)
FROM emp
GROUP BY deptno;


SELECT deptno, MIN(sal) FROM emp
GROUP BY deptno
having min(sal) > (SELECT MIN(sal) FROM emp WHERE deptno = 30);

-- 다중행 서브쿼리: in, exists

-- 업무별로 최대급여를 받는 사원의 사번, 이름, 업무, 급여를 출력하세요
SELECT empno, ename, job, sal
FROM emp
WHERE (job,sal) IN ( SELECT job, MAX(sal) FROM emp GROUP BY job);

-- exists 연산자
-- 서브쿼리의 데이터가 존재하는지 여부를 체크해서 존재하는 겂들만 반환
-- 사원을 관리하는 사원의 정보를 보여주세요

SELECT empno, ename, job FROM emp e
WHERE EXISTS (SELECT empno FROM emp WHERE e.empno = mgr);

-- 다중열 subquery :  2개 이상의 칼럼을 반환하는 서브쿼리

-- 부서별로 최소급여를 받는 사원의 사번, 이름, 부서번호, 업무, 급여를 출력하세요
SELECT empno, ename, deptno, job, sal FROM emp
where sal IN (SELECT MIN(sal) FROM emp GROUP BY deptno);


-- select 문에서 subquery 사용
/* 고객 테이블에 있는 고객 정보 중 마일리지가 
	가장 높은 금액의 고객 정보를 보여주세요.
*/	
SELECT * FROM member;

SELECT * FROM member
WHERE mileage IN (select MAX(mileage) FROM member);

	/* 상품 테이블에 있는 전체 상품 정보 중 상품의 판매가격이 
	    판매가격의 평균보다 큰  상품의 목록을 보여주세요. 
	    단, 평균을 구할 때와 결과를 보여줄 때의 판매 가격이
	    50만원을 넘어가는 상품은 제외시키세요.
	  */  
	
SELECT * FROM products;
/*
SELECT * FROM products
WHERE output_price > 
(select AVG(output_price) FROM products WHERE output_price <= 500000
) and ouput_price <= 500000;
*/
	
	/* 상품 테이블에 있는 판매가격에서 평균가격 이상의 상품 목록을 구하되 평균을
	    구할 때 판매가격이 최대인 상품을 제외하고 평균을 구하세요.*/

SELECT * FROM products WHERE output_price >= (SELECT AVG(output_price) FROM products
WHERE output_price < (SELECT MAX(output_price) FROM products));

/* 상품 카테고리 테이블에서 카테고리 이름에 컴퓨터라는 단어가 포함된 카테고리에
	속하는 상품 목록을 보여주세요.*/
SELECT c.*, p.products_name 
FROM category c JOIN products p
ON c.category_code = p.CATEGORY_FK and category_name LIKE '%컴퓨터%';

SELECT *
FROM products
WHERE category_fk IN 
SELECT category_code FROM category WHERE category_name LIKE '%컴퓨터%');

/*고객 테이블에 있는 고객정보 중 직업의 종류별로 가장 나이가 많은 사람의 정보를
	화면에 보여주세요.*/
SELECT * FROM member;
	
SELECT * FROM member
WHERE age = (SELECT MAX(age) FROM member GROUP BY job);


-- EMP와 DEPT 테이블에서 업무가 MANAGER인 사원의 이름, 업무,부서명,
--	근무지를 출력하세요.

SELECT e.ename, e.JOB, d.dname, d.loc 
FROM emp e JOIN dept d
ON e.deptno = d.deptno
AND job = 'manager';

-- from 절에 사용한 subquery를 inline view라고 한다
-- view와 같은 역할을 하므로 인라인 뷰라고 함


/*
 	1] 고객 테이블에 있는 고객 정보 중 마일리지가 가장 높은 금액을
	     가지는 고객에게 보너스 마일리지 5000점을 더 주는 SQL을 작성하세요.
	     
	MYSQL의 경우 UPDATE나 DELETE시  자기 테이블의 데이터를 바로 사용하지 못한다.
	그래서 서브쿼리의 결과를 별칭을 주어 임시테이블로 저장한 뒤 적용해보자.
	*/
SELECT * FROM member ORDER BY mileage DESC;
-- mariaDB, Oracle
UPDATE member SET mileage = mileage + 5000
WHERE mileage = (SELECT MAX(mileage) FROM member);

-- mysql workbench
UPDATE MEMBER SET MILEAGE = MILEAGE +5000
	WHERE MILEAGE = (SELECT a.* FROM (SELECT MAX(MILEAGE) FROM MEMBER) a);
	SELECT * FROM MEMBER;


/* 고객 테이블에서 마일리지가 없는 고객의 등록일자를 고객 테이블의 
	      등록일자 중 가장 뒤에 등록한 날짜에 속하는 값으로 수정하세요.*/

UPDATE member SET reg_date = (SELECT MAX(reg_date) FROM member)
WHERE mileage = 0;

SELECT * FROM member ORDER BY mileage DESC;
ROLLBACK;


-- delete 문에서 subquery

/* 상품 테이블에 있는 상품 정보 중 공급가가 가장 큰 상품은 삭제 시키는 
	SQL문을 작성하세요.*/
SELECT * FROM products;

delete FROM products
WHERE input_price = (select MAX(input_price) FROM products);


/*  상품 테이블에서 상품 목록을 공급 업체별로 정리한 뒤,
	각 공급업체별로 최소 판매 가격을 가진 상품을 삭제하세요.*/
DELETE FROM products
WHERE output_price IN 
(SELECT MIN(output_price) FROM products GROUP BY ep_code_fk);















