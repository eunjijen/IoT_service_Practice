-- day04_DML.sql
-- DML문장 ( data maipulation language)
-- insert / update / delete / select (DQL-DATA QUERY LANGUAGE)

SELECT * FROM dept;

-- 다른 테이블로부터 복사
-- CREATE TABLE 테이블명
-- AS SELECT * FROM 테이블2;

CREATE TABLE dept2
AS select * FROM dept;

SELECT * FROM dept2;
/*
INSERT INTO 테이블명(컬럼명1, 컬럼명2,..)
VALUES (값1, 값2, ...)

INSERT INTO 테이블명
VALUES(값1, 값2,..)
*/

INSERT INTO dept2
VALUES(50, 'EDUCATION', 'SEOUL');

SELECT * FROM dept2;

INSERT INTO dept2
VALUES(60, 'PLANNING', null);


-- MYSQL은 AUTO COMMIT이 기본설정
SELECT @@AUTOCOMMIT;  -- 1을 반환하면 (AUTO COMMIT), 0(수동으로 COMMIT)
-- AUTO COMMIT은 되돌리지 못해 한번 삭제하면 확정

-- AUTO COMMIT 해제
SET AUTOCOMMIT = 0;

DELETE FROM dept2 WHERE 1=1;
SELECT * FROM dept2;

ROLLBACK;  -- 취소 (TCL - TRANSACTION CONTROL LANGUAGE)

-- DEPT2에서 LOC가 NULL인 데이터를 삭제하세요
DELETE FROM dept2 WHERE LOC is NULL;

COMMIT;  -- 메모리 버퍼에 있던 것이 완전히 반영되어 commit 하면 취소가 안돼

-- DML 문장은 COMMIT, ROLLBACK을 통해 TRANSACTION을 완료해야 한다
-- DDL (CREATE, DROP, ALTER) ==> 즉각적으로 영향을 미친다

-- emp 테이블을 복사해서 emp2를 만들되 테이블 구조만 복사하세요
CREATE TABLE if not exists emp2
AS select * FROM emp WHERE 1=2;

SHOW TABLES;  -- 확인
SELECT * FROM emp2;

-- INSERT INTO 테이블명 subquery

-- EMP에서 10번 부서 사원정보를 가져와서 EMP2에 insert 하세요

INSERT INTO emp2 SELECT * FROM emp WHERE deptno = 10;
SELECT * FROM emp2;  -- 확인

-- emp에서 20번 부서 사원정보 중 사번, 사원명,업무만 가져와서 emp2에 insert
insert INTO emp2 (empno, ename, job, deptno) 
select empno, ename, job, deptno FROM emp
WHERE deptno = 20;

SELECT * FROM emp2;


-- UPDATE 문 
-- 데이터 수정시 사용
-- UPDATE 테이블명 SET 컬럼명1=값1, 컬럼명2=값2,...;
-- UPDATE 테이블명 SET 컬럼명1=값1, 컬럼명2=값2,... WHERE 조건='값'


-- emp2테이블에서 사번이 7788인 사원의 부서번호를 10으로 수정하세요.
UPDATE emp2 SET deptno = 10 WHERE empno = 7788;
COMMIT;
SELECT * FROM emp2;

-- emp2 테이블에서 사번이 7369인 사원의 부서를 10,
-- 급여를 3500으로 변경하여라. 
UPDATE emp2 SET deptno = 10, sal = 3500 WHERE empno = 7369;
SELECT * FROM emp2;

-- emp2테이블에서 부서를 모두 30로 수정하세요
UPDATE emp2 SET deptno = '30';
SELECT * FROM emp2;

ROLLBACK;

SELECT * FROM member;

CREATE TABLE member2 AS SELECT userid id, NAME, mileage point, job, reg_date indate
from member;

SELECT * FROM member2;

-- 1] 고객 중 13/09/01이후 등록한 고객들의 마일리지를 350점씩 올려주세요
UPDATE member2 SET POINT = POINT + 350 WHERE indate > '2013-09-01';
ROLLBACK;

-- 2] 등록되어 있는 고객 정보 중 이름에 '김'자가 들어있는 모든 이름을 '김' 대신
-- '최'로 변경하세요.
SELECT * FROM member2;

UPDATE member2 SET NAME = REPLACE(NAME,'김','최') WHERE 1=1;
ROLLBACK;


-- ----------------------------------------------------------------------------------


-- 1. 고객(MEMBER) 테이블에서 이름이 홍길동이면서 직업이 학생이 정보를 모두 보여주세요.
SELECT * FROM member2
WHERE NAME = '홍길동' and job = '학생';

-- 3. 고객 테이블에서 이름이 홍길동이거나 직업이 학생이 정보를 모두 보여주세요.
SELECT * FROM member2
WHERE NAME = '홍길동' or job = '학생';


-- 3. 상품(PRODUCTS) 테이블에서 제조사(COMPANY)가 삼성 또는 대우 이면서 
-- 판매가가 100만원 미만의 상품 목록을 보여주세요.
SELECT * FROM products;

SELECT * from products 
WHERE company IN( '삼성', '대우') AND output_price < 1000000;

--  4. 상품 테이블에서 배송비의 내림차순으로 정렬하되, 
--  같은 배송비가 있는 경우에는 마일리지의 내림차순으로 정렬하여 보여주세요.
SELECT * FROM products
ORDER BY trans_cost DESC, mileage desc;

-- 5. 상품 테이블에서 공급가가 가장 비싼 순으로 TOP 3안에 드는 상품을 보여주세요
SELECT * FROM products;

SELECT products_name, input_price FROM products
ORDER by input_price desc LIMIT 3;


-- 6. 사원 테이블에서 입사한 년도별로 사원 수를 보여주세요.
SELECT * FROM emp;

SELECT DATE_FORMAT(hiredate,'%Y') ipsa, COUNT(hiredate)
FROM emp GROUP BY ipsa ORDER BY ipsa;

SELECT YEAR(hiredate), COUNT(*)
FROM emp GROUP BY YEAR(hiredate);


-- 7. 사원 테이블에서 해당년도 각 월별로 입사한 사원수를 보여주세요.
SELECT DATE_FORMAT(hiredate, '%Y-%m') ipsa, COUNT(hiredate)
FROM emp GROUP BY ipsa ORDER BY ipsa;


-- 8. 사원테이블에서 현재까지의 근무 일수가 몇 주 몇일인가를 출력하세요.
-- 단 근무일수가 많은 사람순으로 출력하세요.
SELECT ename, ROUND(DATEDIFF(NOW(), hiredate)/7) WEEK, MOD(hiredate,7)DAY
FROM emp order by datediff(NOW(), hiredate) DESC;


-- 9. 사원 테이블에서 83년도에 입사한 사원 정보를 현재 년도 정보로 입사일을 수정하세요
SELECT @@autocommit;

UPDATE emp SET hiredate = NOW() WHERE DATE_FORMAT(hiredate,'%y') = '83';
SELECT * FROM emp;
ROLLBACK;


-- 10. EMP테이블에서 입사일자가 81년도 1월에 입사한 사원의 정보를 삭제하라.
SELECT * FROM emp;

DELETE FROM emp
WHERE date_format(hiredate, '%y-%m') = '81-02';

 -- 11. MEMBER테이블을 카피해서 MEMBER_20 을 만드세요. 단 테이블 구조만 복사하세요

CREATE TABLE member_20
AS SELECT * FROM member WHERE 0 = 1;

SELECT * FROM member_20;

-- 12. 고객 테이블에서 20세 이상인 회원정보들만 가져와서 MEMBER_20에 삽입하세요
 INSERT INTO member_20
 SELECT * FROM member WHERE age >= 20;
 
-- 13. INSERT 해서 회원정보 3명을 추가하세요
INSERT INTO member_20
VALUES(11, 'id11', '김회원', '2354', 22, 500, '직장인', '용인시 수지구', NOW());
INSERT INTO member_20
VALUES(12, 'id12', '김지수', '2954', 27, 5000, '학생', '서울시 강북구', NOW());
INSERT INTO member_20
VALUES(13, 'id13', '김제니', '6827', 23, 10000, '직장인', '수원시 분당구', NOW());


-- 14. PRODUCTS2 사본 테이블을   만들어 실습하세요
CREATE TABLE if not exists products2 AS SELECT *
FROM products;

SELECT * FROM products2;
-- 15. 상품 테이블에 있는 상품 중 상품의 판매 가격이 10000원 이하인 상품을 모두 
-- 	      삭제하세요.
DELETE FROM products2 WHERE output_price <= 10000;

SELECT @@autocommit;
SET autocommit = 0;

-- 16. 상품 테이블에 있는 상품 중 상품의 대분류가 도서인 상품을 삭제하세요.
SELECT * FROM products2;
SELECT * FROM category;

DELETE FROM products2 WHERE category_fk = '00010000';

DELETE FROM products2 
WHERE category_fk = (SELECT category_code FROM category WHERE category_name = '전자제품');

ROLLBACK;

-- 17. PRODUCTS2 에서 가장 비싼 판매가를 가진 상품 정보를 삭제하세요
SELECT products_name, output_price FROM products2 ORDER BY 2 DESC;

DELETE FROM products2 WHERE output_price = (SELECT MAX(output_price) FROM products2);

-- 18. PRODUCTS2 에서 가장 저렴한 판매가를 가진 상품의 판매가를 20% 인상하세요
UPDATE products2 SET output_price = output_price * 1.2
WHERE output_price = (SELECT MIN(output_price) FROM products2);


SELECT * FROM products2;




