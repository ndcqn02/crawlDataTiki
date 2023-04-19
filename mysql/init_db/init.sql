CREATE DATABASE tiki;
USE tiki;
CREATE TABLE product (
id int(10) NOT NULL AUTO_INCREMENT,
title varchar(30) NOT NULL DEFAULT '',
price int(10) NOT NULL,
PRIMARY KEY (id)
);