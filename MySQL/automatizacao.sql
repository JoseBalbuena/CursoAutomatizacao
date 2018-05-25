CREATE DATABASE IF NOT EXISTS automatizacao;
USE automatizacao; 
CREATE TABLE IF NOT EXISTS INTERFACES (id int NOT NULL AUTO_INCREMENT,hostname varchar(50) NOT NULL,interface varchar(50) NOT NULL,ip varchar(50) NOT
 NULL,PRIMARY KEY(ID) );
INSERT INTO INTERFACES (hostname,interface,ip) VALUES ('R1','f0/0','192.168.200.1');
INSERT INTO INTERFACES (hostname,interface,ip) VALUES ('R1','f0/1','12.12.12.1');
INSERT INTO INTERFACES (hostname,interface,ip) VALUES ('R1','lo0','1.1.1.1');
INSERT INTO INTERFACES (hostname,interface,ip) VALUES ('R2','f0/0','12.12.12.2');
INSERT INTO INTERFACES (hostname,interface,ip) VALUES ('R2','lo0','2.2.2.2');

