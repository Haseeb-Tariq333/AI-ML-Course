USE PRIME;
SELECT * FROM CUSTOMERS;
SELECT * FROM ORDERS;

-- Sub Queries
SELECT * FROM orders WHERE amount > ( SELECT AVG(AMOUNT) FROM orders);


-- Views
CREATE VIEW view1 AS
SELECT customer_id, name FROM customers;


SELECT * FROM view1;


CREATE VIEW view3 AS
SELECT c.customer_id, c.name, o.order_id
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

SELECT * FROM view3;

SELECT * FROM ACCOUNTS;

DELIMITER $$
CREATE PROCEDURE check_bal ( IN acc_id INT )
BEGIN
SELECT balance FROM accounts WHERE id = acc_id;
END $$

DELIMITER ;

CALL check_bal(1);