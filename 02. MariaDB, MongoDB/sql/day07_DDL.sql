-- day07_DDL.sql
USE schooldb;

CREATE TABLE bit_table(
id INT,
CODE bit(7)
);

SHOW TABLES;

DESC bit_table;

INSERT INTO bit_table(id,CODE)
VALUES(100,11);

-- 10진수 11을 bit로 바꿔서 저장

SELECT * FROM bit_table;

-- enum ('값1', '값2')

CREATE TABLE if NOT EXISTS reservation(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(30),
	reserve_date DATE,
	room_num SMALLINT UNSIGNED,
	room_type ENUM('single', 'double', 'triple')
);

DESC reservation;

INSERT INTO reservation(NAME, reserve_date, room_num, room_type)
VALUES('이은지',CURDATE(),201,'single');

INSERT INTO reservation(NAME, reserve_date, room_num, room_type)
VALUES('김태형',CURDATE(),303,'triple');

SELECT * FROM reservation;

-- primary key 제약조건 추가
-- unique + not null
-- 자동으로 unique index가 생성

-- 1. 컬럼 수준에서 제약
/*
	CREATE TABLE 테이블명(
		...
		컬럼명 자료형 [CONTRAINT 제약조건이름] 제약조건 유형
		...
		)*/

-- 2. 테이블 수준에서 제약




-- 1. 컬럼 수준에서 제약
CREATE TABLE user_tab4(
	num INT,
	NAME VARCHAR(20),
	passwd VARCHAR(10),
	PRIMARY KEY (num)
	-- CONSTRAINT user_tab2_num_pk PRIMARY KEY(num)
);

DESC user_tab4;

SELECT * FROM user_tab4;


-- foreign key (외래키) 제약조건
-- 부모 테이블 (master table) : 부서(1)
-- 자식 테이블 (detail table) : 사원(N)

CREATE TABLE dept_tab(
	deptno SMALLINT,
	dname VARCHAR(30),
	loc VARCHAR(20),
	PRIMARY KEY (deptno)
);

DESC dept_tab;

CREATE TABLE emp_tab(
	empno INT,
	ename VARCHAR(20) NOT null,
	job VARCHAR(20),
	mgr INT REFERENCES emp_tab(empno),  -- fk
	hiredate DATETIME DEFAULT NOW(),  -- 값을 지정안했을 때 기본값 설정 (현재시간으로)
	sal DECIMAL(7,2),
	comm DECIMAL(7,2),
	deptno SMALLINT, 
	PRIMARY KEY (empno),
	FOREIGN KEY (deptno) REFERENCES dept_tab(deptno)
);

DESC emp_tab;

INSERT INTO dept_tab(deptno, dname, loc)
VALUES(10, 'RESEARCH', 'SEOUL');

INSERT INTO dept_tab(deptno, dname, loc)
VALUES(20, 'SALES', 'INCHEON');

COMMIT;

SELECT * FROM DEPT_TAB;

INSERT INTO EMP_TAB(EMPNO,ENAME,DEPTNO,JOB)
VALUES(8001, '김사원', 10, 'MANAGER');

INSERT INTO EMP_TAB(EMPNO,ENAME,DEPTNO,JOB, MGR)
VALUES(8002, '지수원', 10, 'OPERATOR', 8001);

COMMIT;

INSERT INTO EMP_TAB(EMPNO,ENAME,DEPTNO,JOB)
VALUES(8003, '김태형', 20, 'SALESMAN');

INSERT INTO EMP_TAB(EMPNO,ENAME,DEPTNO,JOB, MGR)
VALUES(8004, '박수원', 20, 'OPERATOR', 8003);

SELECT * FROM EMP_TAB;

-- DEPT_TAB에서 20번 부서를 삭제하세요
DELETE FROM DEPT_TAB WHERE DEPTNO = 20;

UPDATE emp_tab SET deptno = 10 WHERE deptno = 20;

DELETE FROM dept_tab WHERE deptno = 20;

SELECT * FROM dept_tab;

-- 자식레코드가 있는 상태에서 부모 레코드를 삭제하려면 on delete cascade 옵션을 주면 가능
-- 부모 레코드를 삭제할 때 자식 레코드도 같이 삭제됨
CREATE TABLE board(
	num INT PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	content TEXT,
	wdate DATE DEFAULT NOW()
);
DESC board;

-- 댓글 : REPLY
CREATE TABLE REPLY(
	RNUM INT PRIMARY KEY,
	RCONTENT TEXT,
	RDATE DATE DEFAULT NOW(),
	NUM_FK INT REFERENCES BOARD (NUM) ON DELETE CASCADE
);
	
DESC REPLY;

INSERT INTO BOARD VALUES(1,'첫번째 글입니다','냉무',CURDATE());
INSERT INTO BOARD VALUES(2,'두번째 글입니다','냉무',CURDATE());

SELECT * FROM board;


INSERT INTO REPLY
VALUES(201,'2_1안녕!', CURDATE(),2);

SELECT * FROM REPLY;

-- BOARD와 REPLY를 JOIN해서 같이 보여주세요

SELECT B.*, R.*
FROM BOARD B JOIN REPLY R
ON B.NUM = R.NUM_FK;

DELETE FROM BOARD WHERE NUM = 1; -- 글을 지우면 댓글도 없어짐


SELECT * FROM board;

COMMIT;

-- UNIQUE KEY : 데이터의 중복을 허용하지 않는다. NULL값은 허용함
-- UNIQUE INDEX가 자동 생성

CREATE TABLE UNI_TAB(
	DNO INT UNIQUE,  -- 컬럼 수준
	DNAME CHAR(20),
	LOC CHAR(20),
	UNIQUE (DNAME)  -- 테이블 수준
);

DESC UNI_TAB;

INSERT INTO UNI_TAB VALUES(20, 'SALES2', 'SEOUL');  -- 이미 있는 값을 넣을 수 없음

SELECT * FROM UNI_TAB;  -- UNIQUE한 값을 보장

-- NOT NULL : NULL값을 허용하지 않음. 컬럼수준에서만 제약 가능함

CREATE TABLE NN_TAB(
	DNO INT NOT NULL,
	DNAME CHAR(20),
	LOC CHAR(20) NOT NULL
);

DESC NN_TAB;

-- CHECK 제약조건 : 행이 만족해야 하는 조건을 기술

CREATE TABLE MEMBER_TAB(
	IDX INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20) NOT NULL,
	HP1 CHAR(3) CHECK (HP1 IN ('010', '011')),
	HP2 CHAR(4) NOT NULL,
	HP3 CHAR(4) NOT NULL
);

DESC MEMBER_TAB;

INSERT INTO MEMBER_TAB(NAME, HP1, HP2, HP3)
VALUES('만득이','010','1234','1111');

INSERT INTO MEMBER_TAB(NAME, HP1, HP2, HP3)
VALUES('천득이','011','2284','1111');

INSERT INTO MEMBER_TAB(NAME, HP1, HP2, HP3)
VALUES('백득이','011','2864','1111');


CREATE TABLE MEMBER_TAB2(
	IDX INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20) NOT NULL,
	HP1 CHAR(3) NOT NULL,
	HP2 CHAR(4) NOT NULL,
	HP3 CHAR(4) NOT NULL,
	CHECK (HP1 IN ('010', '011'))
);

DESC MEMBER_TAB;

INSERT INTO MEMBER_TAB2(NAME, HP1, HP2, HP3)
VALUES('백득이','011','2864','1111');


SELECT * FROM MEMBER_TAB2;

SHOW TABLES;


-- ALTER 문장 
-- 컬럼 추가/ 변경 / 삭제하고자 할 때 사용 

-- ALTER TABLE 테이블명 ADD 추가할 컬럼정보 
-- ALTER TABLE 테이블명 MODIFY 수정할 컬럼정보
-- ALTER TABLE 테이블명 DROP COLUMN 삭제할 컬럼명
-- ALTER TABLE 테이블명 RENAME COLUMN 예전컬럼명 TO 새컬럼명

-- DEMO_TAB을 생성하되 NAME VARCHAR(20)

CREATE TABLE DEMO_TAB(
	NAME VARCHAR(20)
);

DESC DEMO_TAB;

-- DEMO_TAB에 NO INT 컬럼을 추가하세요
ALTER TABLE DEMO_TAB ADD NO INT;

-- NO 컬럼의 자료형을 CHAR(11)로 수정하세요
ALTER TABLE DEMO_TAB MODIFY NO CHAR(11);

-- NAME컬럼을 삭제하세요
ALTER TABLE DEMO_TAB DROP COLUMN NAME;

-- NO 컬럼의 이름을 NUM으로 변경하세요
ALTER TABLE DEMO_TAB RENAME COLUMN NO TO NUM;

DESC DEMO_TAB;

COMMIT;

USE schooldb;

CREATE TABLE if not exists zipcode(
	post1 CHAR(3),
	post2 CHAR(3),
	addr VARCHAR(100),
	PRIMARY KEY(post1, post2)
);

DESC zipcode;

DROP TABLE if EXISTS member_tab;

CREATE TABLE if NOT EXISTS member_tab(
	id VARCHAR(16) PRIMARY KEY,
	NAME VARCHAR(30),
	gender CHAR(1),
	jumin1 CHAR(6),
	jumin2 CHAR(7),
	tel VARCHAR(15),
	post1 CHAR(3),
	post2 CHAR(3),
	addr1 VARCHAR(100),
	addr2 VARCHAR(100),
	CHECK (gender IN ('F', 'M')),
	UNIQUE (jumin1, jumin2),
	FOREIGN KEY (post1, post2) REFERENCES zipcode(post1, post2)
);

DESC member_tab;

INSERT INTO zipcode VALUES(111,222,'서울 마포구');
INSERT INTO zipcode VALUES(111,223,'서울 서대문구');

SELECT * FROM zipcode;

INSERT INTO member_tab(id, NAME, gender, jumin1, jumin2, post1, post2);
VALUES(1, '홍길동', 'M', 123456, 7891234, 111,222);

INSERT INTO member_tab(id, NAME, gender, jumin1, jumin2, post1, post2);
VALUES(2, '김동희', 'F', 123456, 2891234, 111,222);

INSERT INTO member_tab(id, NAME, gender, jumin1, jumin2, post1, post2);
VALUES(3, '김동희', 'F', 123457, 2893434, 111,223);

SELECT * FROM member_tab;


-- [문제1]
--   EMP테이블에서 부서별로 인원수,평균 급여, 급여의 합, 최소 급여,
--   최대 급여를 포함하는 EMP_DEPTNO 테이블을 생성하라.
DROP TABLE emp_deptno;

CREATE TABLE emp_deptno
AS SELECT deptno, COUNT(*) CNT, AVG(sal) AVG_SAL, SUM(sal) SUM_SAL, 
MIN(sal) MIN_SAL, MAX(sal) MAX_SAL
FROM emp Group BY deptno;

DESC emp_deptno;

-- VIEW 생성
CREATE VIEW 뷰이름
AS
SELECT 컬럼명1, 컬럼명2,...FROM 테이블명 WHERE 조건절

-- VIEW 삭제
-- DROP VIEW 뷰이름;

SELECT * FROM emp;

-- EMP 테이블에서 20번 부서의 모든 컬럼을 포함하는 EMP20_VIEW를 생성하라
CREATE VIEW emp20_VIEW
AS
SELECT * FROM emp WHERE deptno = 20;

SELECT * FROM emp20_view;

SET autocommit = 0;
UPDATE emp SET deptno = 10 WHERE ename = 'smith';

rollback;

-- emp 테이블에서 30번 부서인 empno를 emp_no로 ename를 name으로 sal을 salary로 바꾸어
-- emp30_view를 생성하여라
CREATE OR REPLACE VIEW emp30_view
AS
SELECT empno emp_no, ename NAME, sal salary FROM emp
WHERE deptno = 30;

SELECT * FROM emp30_view;

-- 고객테이블의 고객 정보 중 나이가 19세 이상인 고객의 정보를 확인하는 뷰를 만들자
-- 단 뷰의 이름은 member_19

CREATE OR REPLACE VIEW MEMBER_19_VW
AS
SELECT * FROM member WHERE AGE >= 19;

SELECT * FROM MEMBER_19_VW;

UPDATE MEMBER_19_VW SET AGE = 19 WHERE NUM = 1;

SELECT * FROM member;

UPDATE member SET AGE = 18 WHERE NUM = 2;

-- WITH CHECK OPTION절을 이용
-- WHERE 조건절에 위배되는 데이터가 들어오지 못하도록 제약한다
CREATE OR REPLACE VIEW MEMBER_19_VW
AS SELECT * FROM member WHERE AGE >= 19 
WITH CHECK OPTION;


SELECT * FROM MEMBER_19_VW;

UPDATE MEMBER_19_VW SET AGE = 18 WHERE NUM = 1;
-- 에러 발생 R

-- 뷰 소스 확인
SHOW CREATE VIEW MEMBER_19_VW;

-- category와 products, supply_comp 3개의 테이블을 join하여
-- view 를 생성하세요. products_info_view

CREATE OR REPLACE VIEW products_info_view
as
SELECT c.*, products_name, output_price, s.ep_name
FROM category c JOIN products p
ON c.category_code = p.CATEGORY_FK
JOIN supply_comp s
ON p.EP_CODE_FK = s.ep_code;

SELECT * FROM products_info_view;

SELECT * FROM products_info_view WHERE category_name = 'tv';

DROP VIEW member_19_vw;

-- 인덱스 생성
-- DROP INDEX 인덱스명

-- 주의 : 인덱스는 not nulll인 칼럼에만 사용할수있음
-- 고객 테이블에서 name 컬럼에 인덱스를 만드세요

CREATE INDEX name_idx ON member(NAME);

SELECT * FROM member WHERE NAME LIKE '%동%';

DROP INDEX name_idx ON member;

ALTER TABLE member DROP INDEX name_idx;

SHOW INDEX FROM member;
SHOW INDEX FROM member_tab;



