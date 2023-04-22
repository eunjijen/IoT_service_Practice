CREATE DATABASE pybo_db;

CREATE USER 'iot'@'%' IDENTIFIED BY '1234';


GRANT ALL privileges ON iot_db.* TO 'iot'@'%';