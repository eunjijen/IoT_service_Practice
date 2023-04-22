-- day03_function.sql

-- 단일행 함수 : 숫자형 함수 

-- 절대값ㅇ르 구하는 함수 
SELECT ABS(1), ABS(-1);

-- 반올림 함수 : round(값), round(값,n)
SELECT ROUND(3.1415921); -- 소수점 첮째자리에서 반올림, 정수를 반환 
SELECT ROUND(3.1415921, 3); -- 소수점 셋째자리까지 출력 (넷째자리에서 반올림)

SELECT ROUND(4547.567), ROUND(4567.567,0), 
ROUND(4567.567,2), ROUND(4567.567,-2);

-- ceil() : 올림값, floor(): 내림값 
SELECT CEIL(123.0001), FLOOR(123.0001);

-- rand(): 0~1까지의 임의의 난수인 실수값을 반환
SELECT RAND();
-- 1~7까지의 정수를 발생시켜보기
select rand() * 7;

-- rand() * 범위 + 시작수
SELECT FLOOR(RAND()*7 + 1);

-- power(x,y) : x의 y숭
SELECT POWER(2,8), POWER(10,-3);

-- sqrt(n): n의 제곱근을 구함
SELECT SQRT(64), SQRT(13);

/*
ROW_NUMBER() over(분석절)함수: 분석절에 대한 각 행의 번호를 반환
RANK() over(분석절) : 파티션에 대한 순위 값을 매긴다
*/

SELECT ROW_NUMBER() over(ORDER BY sal DESC) rnum, e.* FROM emp e;
-- 보너스 제일 많이 받는 사람 3위까자ㅣ 
SELECT RANK() over(ORDER BY comm DESC) rnk, e.* FROM emp e LIMIT 3;

SELECT ename, comm FROM emp ORDER BY comm DESC;

-- 문자열 함수
-- concat(): 문자열을 결합하는 함수

SELECT CONCAT(ename, job) FROM emp;   -- SMITHCLERK, ALLENSALESMAN

-- 사웜명, 급여 정보를 보여주되 '$'기호를 붙여 보여주세요
SELECT ename, CONCAT('$', sal) FROM emp;

-- left(문자열, len): 문자열의 왼쪽부터 명시한 개수(len)만큼의 문자를 추출해서 반환
-- right(문자열, len): 

SELECT LEFT('mysql python html css', 5), RIGHT('mysql python html css', 5);

SELECT CONCAT(LEFT(ename,2), '***') FROM emp;

-- replace(컬럼, x, y) : 컬럼값 중 x값에 해당하는 단어를 y로 교체한다
-- 실제로 데이터를 수정하는 것은 아님 그냥 교체해서 출력해주는 것

-- 사원 테이블에서 job 중에 'A'를 '$'로 바꿔 출력하기
SELECT ename, job, REPLACE(job,'A','$') FROM emp;
-- update emp set job = replace(job,'A','$') where 1=1;  where 1=1 은 항상 true인 것
-- 로 하면 실제 데이터가 바뀌어
SELECT * FROM emp;

-- format(숫자, n) : 숫자 데이터를 3자리마다 콤마(,)를 붙여 표현한다
SELECT FORMAT(1000000,0);
SELECT FORMAT(123456.12745,2);

-- substring(문자열, start(시작값), len)
SELECT ename, SUBSTRING(ename, 3, 2) FROM emp;

-- # 3. 날짜, 시간 함수
-- 현재 시스템의 날짜와 시간을 구하는 함수`
-- CURDATE(): 현재 년-월-일을 반환
-- CURTIME(): 현재 시:분:초를 반환
-- NOW() : 년-월-일 시:분:초
-- SYSDATE() : 년-월-일 시:분:초

SELECT NOW(), SYSDATE();
SELECT CURDATE();
SELECT CURTIME();

SELECT MONTH(NOW()), YEAR(NOW()), DAY(NOW()), HOUR(now()), MINUTE(NOW()),
second(NOW());

-- 요일 정보: dayname()
SELECT DAYNAME(NOW());

-- 오늘을 기준으로 15일 뒤 날짜를 구하려고 할 때
-- ADDDATE() : 더한 날짜를 반환
-- SUBDATE() : 뺀 날짜

SELECT ADDDATE('2023-02-08', INTERVAL 15 DAY);  -- 2023-02-23
SELECT ADDDATE(NOW(), INTERVAL 15 DAY);  -- 2023-02-23 14:30:38
SELECT SUBDATE(NOW(), INTERVAL 15 DAY);  -- 2023-01-24 14:31:52

-- timediff(시간1, 시간2)
-- datediff(날짜1, 날짜2)
-- 오늘부터 생일까지 며칠이 남았는지 계산해보자 
SELECT DATEDIFF(NOW(), '2023-12-31');  -- -326

-- 오늘부터 3.1절까지 며칠이 남았는지 계산해보자 
SELECT DATEDIFF(NOW(), '2023-03-01');

-- 현재시간부터 강의 마치는 시간까지 얼마남았는지 계산 
SELECT TIMEDIFF('17:50:00', CURTIME());  -- 03:15:15

-- 변환 함수 
-- date_format(날짜시간, 포맷형식)
-- time_format(시간, 포맷형식)
SELECT DATE_FORMAT('20120731', '%Y/%m/%d');  -- 2012/07/31

-- --------------------------------------------------------------------------
-- 그룹 함수 
-- 여러 행 또는 테이블 전체에 함수가 적용되어 하나의 결과를 가져오는 함수 
-- count()
-- avg()
-- sum()
-- max()
-- min()
-- stddev() : 표준편차
-- varance() : 분산값

SELECT COUNT(empno) FROM emp;

SELECT COUNT(mgr) FROM emp;

-- count() 함수는 null값은 세지 않는다
-- count(*) 함수는 null값도 포함해서 센다
-- mgr: 상사 번호
SELECT empno, ename, mgr FROM emp;

SELECT * FROM emp;

CREATE TABLE test_tab(
a INT,
b INT,
c INT);

SELECT * FROM test_tab;

INSERT INTO test_tab(a,b,c) VALUES(NULL,NULL,NULL);

SELECT COUNT(a) FROM test_tab;  -- null값을 제외하고 count
SELECT COUNT(*) FROM test_tab;

SELECT COUNT(mgr) FROM emp;

-- emp테이블에서 모든 SALESMAN에 대하여 급여의 평균,
-- 최고액,최저액,합계를 구하여 출력하세요.
SELECT AVG(sal) FROM emp WHERE job = 'salesman';
SELECT max(sal) FROM emp WHERE job = 'salesman';
SELECT min(sal) FROM emp WHERE job = 'salesman';
SELECT sum(sal) FROM emp WHERE job = 'salesman';

-- EMP테이블에 등록되어 있는 인원수, 보너스에 NULL이 아닌 인원수,
-- 보너스의 평균,등록되어 있는 부서의 수를 구하여 출력하세요.
SELECT COUNT(empno), COUNT(comm), AVG(comm), COUNT(DISTINCT deptno) FROM emp;

SELECT MIN(ename), MAX(ename), MIN(hiredate), MAX(hiredate) FROM emp;

-- group by 절
-- 특정 컬럼이나 값ㅇ르 기준으로 레코드를 묶어서 데이터를 관리할 때 사용하는 구문
-- GROUP BY에서 사용될 컬럼과 그룹함수만 SELECT할 수 있다 - 에러는 안남ename 해도

-- 업무별 인원수를 출력해보여주세요
-- WGHOL 순서

SELECT job,COUNT(*) FROM emp
GROUP BY job ORDER BY 2;

-- 부서별 인원수와 최대 급여, 최소급여, 평균 급여를 보여주세요
SELECT COUNT(*),MAX(sal), MIN(sal),round(AVG(sal)) FROM emp
GROUP BY job ORDER BY 2;

SELECT deptno, COUNT(*),MAX(sal), MIN(sal),round(AVG(sal)) FROM emp
GROUP BY deptno ORDER BY 2;


-- 고객(member) 테이블에서 직업(JOB)별 최대 마일리지(MILEAGE) 정보를 출력하세요
SELECT job, max(mileage) FROM member
GROUP BY job;


SELECT * FROM category; -- category code가 0으로 끝나는 것이 대분류 

-- 상품(PRODUCTS) 테이블에서 카테고리별(category_fk)로 총 몇 개의 상품이 있는지 
-- 또한 최대 판매가(OUTPUT_PRICE)와 최소 판매가를 함께 보여주세요.
SELECT category_fk, COUNT(*), MAX(output_price), MIN(output_price) 
FROM products 
GROUP BY category_fk;


-- HAVING 절 
-- GROUP BY와 항상 함께 사용하는 구문 
-- GROUP BY의 결과에 조건을 주어 제한하고자 할 때 사용 

-- 부서별로 인원수가 4명 이상인 부서 정보 
SELECT deptno, COUNT(empno) FROM emp
GROUP BY deptno HAVING COUNT(empno) >= 4 ;


-- 고객 테이블에서 직업의 종류와 각 직업에 속한 사람의 수가  3명 이상인 직업군
--    의 정보를 보여주시오.
SELECT job, COUNT(*) FROM member
GROUP BY job HAVING COUNT(*) >= 3;
		
-- 고객 테이블에서 직업의 종류와 각 직업에 속한 최대 마일리지 정보를 보여주세요.
--   단, 직업군의 최대 마일리지가 0인 경우는 제외시킵시다.
SELECT job, MAX(mileage) FROM member
GROUP BY job HAVING MAX(mileage) <> 0;

--  상품 테이블에서 각 카테고리별로 상품을 묶은 경우, 해당 카테고리의 상품이 2개인 
--  상품군의 정보를 보여주세요.
SELECT category_fk, COUNT(*) FROM products
GROUP BY category_fk HAVING COUNT(category_fk) = 2;
  
--  상품 테이블에서 각 공급업체 코드별(EP_CODE_FK)로 상품 판매가의 평균값 중
-- 단위가 100단위로 떨어지는 항목의 정보를 보여주세요.
--    ** 나머지값 구하는 연산자: %, mod(값1, 값2)함수
SELECT * FROM supply_comp;
SELECT * FROM products;

SELECT ep_code_fk, AVG(output_price) FROM products
GROUP BY ep_code_fk HAVING AVG(output_price) % 100 = 0;
-- HAVING MOD(AVG(output_price), 100) = 0



