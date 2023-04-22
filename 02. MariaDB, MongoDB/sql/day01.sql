USE schooldb;

SHOW TABLES;

CREATE TABLE if NOT EXISTS student(
id INT PRIMARY KEY AUTO_INCREMENT, -- 자동증가 
NAME VARCHAR(30) NOT NULL,
tel VARCHAR(15) NOT NULL,
cname VARCHAR(50),
croom INT);

SHOW TABLES;

DESC student;

SELECT * FROM student;

INSERT INTO student(NAME,tel,cname,croom)
VALUES('홍길동','1111','IOT반',301);

ROLLBACK; --취소
COMMIT; -- 확정
-- transaction control language
/*
여러 라인
주석 처리
mysql은  auto commit 이 된다 oracle은 수동 commit
*/
-- 단문 주석

INSERT INTO student(NAME,tel)
VALUES('이미나','2222');

SELECT * FROM student;

-- 빅데이터반 2명 삽입 301
INSERT INTO student(NAME,tel,cname,croom)
VALUES('박지혜','2222','빅데이터반',301);
INSERT INTO student(NAME,tel,cname,croom)
VALUES('최길동','3222','빅데이터반',301);

-- IOT반도 2명 삽입    302
INSERT INTO student(NAME,tel,cname,croom)
VALUES('이호석','4222','IOT반',302);

INSERT INTO student(NAME,tel,cname,croom)
VALUES('이석철','5222','IOT반',302);

-- AI반 2명 삽입       303

INSERT INTO student(NAME,tel,cname,croom)
VALUES('김명호','5222','AI반',303);
INSERT INTO student(NAME,tel,cname,croom)
VALUES('이호석','5222','AI반',303);

SELECT * FROM student;

-- 데이터 삭제
-- DELETE FROM 테이블명 WHERE 컬럼명=값

DELETE FROM student WHERE id=2;

SELECT * FROM student;

DELETE FROM student WHERE cname='AI반';


-- 데이터 수정
-- UPDATE 테이블명 SET 컬럼명1=수정할값1, 컬럼명2=값2
-- WHERE 컬럼명3=값3

--학번이 3번인 학생의 연락처와 학급명,교실번호를 수정하세요
UPDATE student SET TEL='7878', CNAME='빅데이터반', CROOM=301 WHERE ID=3;

UPDATE student SET CROOM=302 WHERE ID=1;

SELECT * FROM student;

-- 총학생수를 구하시오
SELECT COUNT(ID) FROM student;

-- IOT반 학생수를 구하시오

SELECT COUNT(ID) FROM student WHERE CNAME='IOT반';
SELECT COUNT(ID) FROM student WHERE CNAME='빅데이터반';
SELECT COUNT(ID) FROM student WHERE CNAME='AI반';

-- 학급별 인원수를 출력하세요
-- GROUP BY절을 이용
SELECT CNAME, COUNT(ID) FROM student
GROUP BY CNAME;

-- IOT 반 학생들 교실을 201호로 수정하세요

UPDATE student SET CROOM=201 WHERE CNAME='IOT반';

SELECT * FROM student;

INSERT INTO student(NAME,TEL,CNAME,CROOM)
VALUES('사진희','3333','IOT',302);

-- 데이터의 무결성을 위해
-- 2개의 테이블로 정규화를 해보자 

-- student 테이블을 삭제하세요
-- DROP TABLE 테이블명;
DROP TABLE student;

SHOW TABLES;

/* 학생은 학급에 소속되어 있다
학급 테이블								학생 테이블 
 - 학급번호 (pk)							-  학번(PK)
 - 학급명									 -  이름
 - 교실번호									-  연락처	
												 - 학급번호 (FK- FOREIGN KEY) 외래키
*/
CREATE TABLE IF NOT EXISTS SCLASS(
	SNUM INT PRIMARY KEY AUTO_INCREMENT,
	SNAME VARCHAR(50) NOT NULL,
	SROOM INT
);

SHOW TABLES;
DESC sclass;

CREATE TABLE if NOT EXISTS student(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(30) NOT NULL,
	tel VARCHAR(15) NOT NULL,
	snum_fk INT REFERENCES sclass (snum) -- 외래키 설정
);
DESC student;


/*
학급 데이터를 삽입하기
IOT반 201
빅데이터반 301
AI반 302
*/
INSERT INTO SCLASS(SNAME,SROOM)
VALUES('IOT반',201);

INSERT INTO SCLASS(SNAME,SROOM)
VALUES('빅데이터반',301);

INSERT INTO SCLASS(SNAME,SROOM)
VALUES('AI반',302);

SELECT * FROM SCLASS;

-- 학생 데이터 삽입하기
-- 학생2명 IOT반에 등록하세요

INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('김철수','1111',1);

INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('김수희','2111',1);

SELECT * FROM student;


INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('이수남','3111',2);
INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('박희철','4111',2);


INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('남진','5111',3);
INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('박재신','6111',3);
INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('이수남','3111',3);

INSERT INTO student(NAME,TEL,SNUM_FK)
VALUES('박희철','4111',3);

SELECT * FROM student;

SELECT * FROM  SCLASS;


-- INSERT INTO student(NAME,TEL,SNUM_FK)
-- VALUES('박희철','7111',4);
-- 외래키 제약조건에 위배되는 데이터 삽입을 할 수없음

-- JOIN 문을 이용해서 학급, 학생 테이블을 하나로 만들어서 조회해보자


















