/* chapter17/mydb-mysql-schema-gbk.sql */

/* �������ݿ� */
CREATE DATABASE  IF NOT EXISTS  MyDB;

use MyDB;

/* �û��� */
CREATE TABLE IF NOT EXISTS user (
name varchar(20),     /* �û�Id  */
userid int,	          /* �û����� */
PRIMARY KEY (userid));

/* �����ʼ���� */
INSERT INTO user VALUES('Tom',1);
INSERT INTO user VALUES('Ben',2);