USE instagram;

-- WHERE CLAUSE
SELECT * FROM user WHERE ID=101;
SELECT * FROM user WHERE followers >= 200;

-- OPERATORS
SELECT name,age,followers FROM user WHERE age>15 AND followers >= 200;
SELECT name, age FROM user WHERE age BETWEEN 15 AND 20;
SELECT name,age FROM user WHERE age>15 LIMIT 2;

-- LIMIT
SELECT name, age, followers FROM user ORDER BY followers ASC;

-- AGGREGATE FUNCTIONS
SELECT MAX(Followers) FROM user;
SELECT MIN(followers) FROM user;
SELECT COUNT(name) FROM user;

-- GROUP BY CLAUSE
SELECT  COUNT(id) FROM user GROUP BY age;
SELECT age, MAX(Followers) FROM user GROUP BY age;

-- HAVING CLAUSE
SELECT age, MAX(Followers) FROM user GROUP BY age HAVING MAX(Followers) > 150;

-- UPDATE COMMAND
UPDATE user
SET followers = 500 WHERE age = 15;

-- DELETE
DELETE FROM user WHERE age = 15;

-- ALTER
ALTER TABLE user
ADD COLUMN city VARCHAR(100);

ALTER TABLE user
RENAME TO user_info;

ALTER TABLE user_info
RENAME TO user;

ALTER TABLE user
DROP COLUMN city;

ALTER TABLE user
CHANGE COLUMN name user_name VARCHAR(100) NOT NULL;

ALTER 

SELECT * FROM USER;
INSERT INTO user
VALUES 
(103, "DANYAL", "def@gmail.com", 250, 450, 15 ),
(104,"Ali","ghi@gmail,com",90,100,30);
