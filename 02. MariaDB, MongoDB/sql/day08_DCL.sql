-- day08_DCL.sql

-- root 계정: 관리자 계정 
-- mysql 데이터베이스: 전체 dbms를 관리하는 데이터베이스, root 관리자만 사용할 수 있음
-- mysql에는 user 테이블 ==> 사용자에 대한 정보를 가지고 있음 
--    db 테이블 ==> 사용자가 이용할 데이터베이스 정보를 가짐

SHOW DATABASES;

USE mysql;
SHOW TABLES;
SELECT * FROM USER;
SELECT * FROM db;

-- 사용자 추가
-- create user 사용자명@host identified by '비밀번호'

-- scott/tiger
-- localhost = 127.0.0.1

CREATE USER scott@localhost 
IDENTIFIED BY 'tiger';

SELECT * FROM USER;

-- 외부에서도 접근할 수 있도록 하려면 host에 '%'로 하여 똑같은 계정을 추가한다
CREATE USER 'scott'@'%'
IDENTIFIED BY 'tiger';

-- 사용자 삭제
-- drop user 사용자명;

-- 사용자를 추가하세요 'KING' 비번 '1234' 생성하되 
-- 로컬과 외부에서 접속할 수 있도록 생성하세요
CREATE USER king@localhost
identified BY '1234';

CREATE USER 'king'@'%'     -- 외부에서도 접근 가능한 user
identified BY '1234';
-- user에서 조회
SELECT * FROM USER;
-- king을 다시 drop
DROP USER king@localhost;
DROP USER 'king'@'%';

-- 데이터베이스 생성
-- CREATE datebase 데이터베이스명 default character utf8;

CREATE DATABASE multidb;

SHOW DATABASES;

-- scott 사용자에게 multidb 데이터베이스를 사용할 권한을 부여해보자
-- DCL : GRANT, REVOKE
-- 권한 부여 : GRANT ALL PRIVILEGES ON DB명.테이블명 TO 계정아이디@HOST
-- 권한 부여 적용 FLUSH PRIVILEGES
-- 사용자에게 부여한 권한 확인: SHOW GRANTS FOR 계정아이디@HOST


-- multidb 데이터베이스에 대한 모든 권한을 scott에게 부여하세요
-- 적용하고 확인해보세요
GRANT ALL PRIVILEGES ON multidb.* TO scott@localhost;
FLUSH PRIVILEGES;

SHOW GRANTS FOR scott@localhost;
USE mysql;

SELECT * FROM db;

-- 권한 회수
-- REVOKE ALL ON 데이터베이스명.* FROM 계정아이디@HOST

REVOKE ALL ON multidb.* FROM scott@localhost;















