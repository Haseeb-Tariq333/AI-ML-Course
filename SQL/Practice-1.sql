CREATE DATABASE college;
USE college;

CREATE TABLE student(
roll_no INT,
name VARCHAR(30),
age INT 
);

INSERT INTO student
VALUES
(101, "Haseeb", 19),
(102, "Habib", 20);

SELECT * FROM student;

DROP DATABASE college;

CREATE DATABASE instagram;
USE instagram;

CREATE TABLE user(
ID INT PRIMARY KEY,
Name VARCHAR(30) NOT NULL,
EMAIL VARCHAR(30) UNIQUE,
Followers INT DEFAULT 0,
Following INT,
age INT,
CONSTRAINT age_check CHECK (age>13) 
);

INSERT INTO user 
VALUES
(101, "Haseeb", "chaudhryhaseeb4116@gmail.com", 200, 500,19),
(102, "Habib", "abc@gmail.com",100,230,22);

SELECT * FROM user;


CREATE TABLE posts(
id INT PRIMARY KEY,
content VARCHAR(1000),
user_id INT,
FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO posts
VALUES
(1, "HELLO",101),
(2, "BYE",102);

SELECT * FROM posts;


