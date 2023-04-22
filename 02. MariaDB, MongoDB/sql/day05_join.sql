-- day05_join.sql

/*
구문
	SELECT table1.colum1[, table2.column2 ...]
	FROM	  table1, table2
	WHERE table1.colum1=table2.column2;

	또는 join절을 이용한 명시적 조인

	SELECT table1.colum1[,table2.colum2...]
	FROM table1 JOIN table2 
	ON  table1.column1 = talbe2.column2;

*/

-- equi join
SELECT * FROM emp;
SELECT * FROM dept;

SELECT emp.ename, job, sal, dept.deptno, dname, loc 
FROM dept, emp
WHERE dept.deptno = emp.deptno ORDER BY dept.deptno;

SELECT d.*, e.*
FROM dept d, emp e
WHERE d.deptno = e.deptno ORDER BY 1;

-- 명시적 join절 사용 (표준 sql)

SELECT d.DEPTNO, dname, ename, job, loc 
FROM dept d JOIN emp e
ON d.deptno = e.deptno ORDER BY 1 DESC;

-- JOIN조건에  AND 를 이용해서 추가적인 조건을 준다.
-- WHERE 절을 이용해서 추가적인 조건을 줄 수도 있다.

-- SALESMAN의 사원번호,이름,급여,부서명,근무지를 출력하여라.
SELECT empno, ename, sal, dname, loc 
FROM dept d JOIN emp e
ON d.deptno = e.deptno AND e.job = 'salesman' 
ORDER BY 1 DESC;

-- 상품 정보를 보여주되 해당 상품의 카테고리명을 함께 보여주세요
SELECT * FROM products;

SELECT c.category_name, p.*
FROM category c JOIN products p
ON c.category_code = p.category_fk ORDER BY 3;

-- 카테고리 테이블과 상품 테이블을 조인하여 화면에 출력하되 상품의 정보 중
-- 제조업체가 삼성인 상품의 정보만 추출하여 카테고리 이름과 상품이름, 상품가격
-- 제조사 등의 정보를 화면에 보여주세요.
SELECT c.category_name, p.*
FROM category c JOIN products p
ON c.category_code = p.category_fk AND p.company = '삼성';


-- cross join(cartesian product)

SELECT dept.*, emp.*
FROM dept, emp ORDER BY 1;

-- non equi join : '='가 아닌 연산자를 이용해서 조인할 경우
-- emp, salgrade

SELECT * FROM salgrade;

-- 각 사원의 사번, 이름, 급여, 급여 등급 정보를 보여주세요
SELECT empno, ename, sal, grade, losal, hisal
FROM emp e JOIN salgrade s
ON e.sal BETWEEN s.losal AND s.hisal ORDER BY grade desc;

-- outer join : equi join으로 조인할 경우 한쪽 테이블에 일치하는 행이 없으면 출력이 안된다
-- 				: outer join의 경우는 일치하는 행이 없으면 다른쪽 테이블을 null로 하여 그 값을 보여줌
-- (회사 시험 문제 많이 나옴)

-- 1. LEFT OUTER JOIN : 왼쪽 테이블을 기주능로 출력
-- 2. RIGHT OUTER JOIN: 오른쪽 테이블을 기눚으로 출력
-- 3. FULL OUTER JOIN : 양쪽 테이블을 기준으로 출력 --> mysql은 이건 없음

SELECT d.DEPTNO, dname, ename, e.deptno
FROM dept d left outer join emp e
on d.deptno = e.deptno ORDER BY 1;


SELECT d.DEPTNO, dname, ename, e.deptno
FROM dept d right outer join emp e
on d.deptno = e.deptno ORDER BY 1;

SELECT DISTINCT(e.deptno), d.deptno
FROM dept d left outer JOIN emp e
ON d.deptno = e.deptno;


SELECT DISTINCT(e.deptno), d.deptno
FROM dept d right outer JOIN emp e
ON d.deptno = e.deptno;

/*
SELECT DISTINCT(e.deptno), d.deptno
FROM dept d full outer JOIN emp e
ON d.deptno = e.deptno;
*/ -- ==> oracle의 경우

-- mysql의 경우는 full outer join을 union을 이용한다

SELECT DISTINCT(e.DEPTNO) FROM emp e
LEFT OUTER JOIN dept d ON e.deptno = d.DEPTNo
UNION
SELECT DISTINCT(d.DEPTNO) FROM emp e
right OUTER JOIN dept d ON e.deptno = d.DEPTNo; -- 합집합

-- self join : 자기 테이블과 join

-- 사원정보를 보여주되, 사번, 사원이름, 사원의 관리자이름을 함께 보여주세요

select empno, ename, mgr FROM emp;

SELECT e.EMPNO, e.ENAME, e.mgr, m.empno, m.ename
FROM emp e JOIN emp m
ON e.mgr = m.empno;

--  상품테이블의 모든 상품을 공급업체, 공급업체코드, 상품이름, 
--  	상품공급가, 상품 판매가 순서로 출력하되 공급업체가 없는
--  	상품도 출력하세요(상품을 기준으로).
SELECT * FROM products;
SELECT * FROM supply_comp;

SELECT s.ep_name, ep_code, products_name, input_price, output_price
FROM supply_comp s JOIN products p
ON s.ep_code = p.ep_code_fk;


SELECT s.ep_name, ep_code, products_name, input_price, output_price
FROM supply_comp s right JOIN products p
ON s.ep_code = p.ep_code_fk;

SELECT s.ep_name, ep_code, products_name, input_price, output_price
FROM supply_comp s left JOIN products p
ON s.ep_code = p.ep_code_fk;

-- 상품테이블의 모든 상품을 공급업체, 카테고리명, 상품명, 상품판매가
-- 순서로 출력하세요. 단, 공급업체나 상품 카테고리가 없는 상품도
-- 출력합니다.
SELECT category_name, products_name, output_price, ep_name
FROM category c right outer JOIN products p
ON c.category_code = p.CATEGORY_FK
left outer JOIN supply_comp s
ON p.ep_code_fk = s.ep_code
ORDER BY 1;

-- emp테이블에서 "누구의 관리자는 누구이다"는 내용을 출력하세요.
-- "SMITH의 관리자는 FORD입니다"

SELECT concat(e.ename,'의 관리자는 ', m.ename, '입니다')
FROM emp e JOIN emp m
ON e.mgr = m.empno;


-- [종합문제]
-- 1. emp테이블에서 모든 사원에 대한 이름,부서번호,부서명을 출력하는 
--    문장을 작성하세요.
SELECT * FROM emp;
SELECT * FROM dept;

SELECT CONCAT(e.ename,'의 부서번호는 ', e.deptno, ' 부서명은 ', d.dname,'입니다.')
from emp e JOIN dept d
ON e.deptno = d.deptno;


-- 2. emp테이블에서 NEW YORK에서 근무하고 있는 사원에 대하여 이름,업무,급여,
--    부서명을 출력하는 SELECT문을 작성하세요.
SELECT e.ename, e.job, e.sal, d.dname, d.loc
FROM emp e JOIN dept d 
ON e.deptno = d.deptno AND d.loc = 'new york' ORDER BY 1;


-- 3. EMP테이블에서 보너스를 받는 사원에 대하여 이름,부서명,위치를 출력하는
--     SELECT문을 작성하세요.
SELECT * FROM emp;
SELECT * FROM dept;

SELECT e.ename, e.job, e.sal, d.dname, d.loc, comm
FROM emp e JOIN dept d 
ON e.deptno = d.deptno WHERE e.COMM > 0;


-- 4. EMP테이블에서 이름 중 L자가 있는 사원에 대해 이름,업무,부서명,위치를 
--    출력하는 문장을 작성하세요.

SELECT e.ename, e.job, d.dname, d.loc
FROM emp e JOIN dept d 
ON e.deptno = d.deptno AND e.ename LIKE '%L%';

/*5. 아래의 결과를 출력하는 문장을 작성하에요(관리자가 없는 King을 포함하여
	모든 사원을 출력)
	---------------------------------------------
	Emplyee		Emp#		Manager	Mgr#
	---------------------------------------------
	KING		7839
	BLAKE		7698		KING		7839
	CKARK		7782		KING		7839
	.....
	---------------------------------------------
*/
SELECT e.ename employee, e.empno "emp#", m.MGR manager, m.EMPNO "Mgr#" 
FROM emp e left outer JOIN emp m
ON e.mgr = m.empno ORDER BY 1;












