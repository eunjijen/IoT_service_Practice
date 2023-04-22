USE schooldb;

SHOW TABLES;

CREATE TABLE if not exists student(
id INT PRIMARY KEY AUTO_INCREMENT, -- 자동 증가
NAME VARCHAR(30) NOT NULL,
tel VARCHAR(15) NOT NULL,
cname VARCHAR(50),
croom INT);

SHOW TABLES;

DESC student;


