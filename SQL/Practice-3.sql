CREATE DATABASE prime;
USE prime;

CREATE TABLE accounts (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
balance DECIMAL (10, 2)
);

INSERT INTO accounts (name, balance) VALUES 
('Haseeb', 500.00),
('Habib', 1000.00),
('Danyal', 1000.00);

SELECT * FROM accounts;

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

COMMIT;

SELECT * FROM accounts;


START TRANSACTION;
UPDATE accounts SET balance =  balance + 1000 WHERE id =1;
UPDATE accounts SET balance = balance -1000 WHERE id =2;
SAVEPOINT error_in_cashback;

UPDATE accounts SET balance = balance + 10 WHERE id = 2;
ROLLBACK TO error_in_cashback;

COMMIT;


