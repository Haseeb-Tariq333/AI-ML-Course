CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers 
(customer_id, name, city) 
VALUES 
(1, 'Haseeb', 'Islamabad'),
(2, 'Habib', 'Lahore'),
(3, 'Ahmed', 'Karachi'),
(4, 'Danyal','Faisalabad');


CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders 
(order_id, customer_id, amount) 
VALUES
(101, 1, 500),
(102, 1, 750),
(103, 2, 950),
(104, 5, 1050);


SELECT * FROM customers;
SELECT * FROM orders;

-- INNER JOIN
SELECT c.customer_id, c.name, o.order_id
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT *
FROM orders AS o
RIGHT JOIN customers AS c
ON o.customer_id = c.customer_id;


SELECT *
FROM orders AS o
RIGHT JOIN customers AS c
ON o.customer_id = c.customer_id
UNION
SELECT *
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.customer_id;


-- CROSS JOIN
SELECT * 
FROM customers
CROSS JOIN orders;

-- SELF JOIN
SELECT * 
FROM customers as A 
JOIN customers as B
ON A. customer_id = B.customer_id;

USE prime;

-- RIGHT EXCLUSIVE JOIN
SELECT * 
FROM customers AS A 
RIGHT JOIN orders AS B 
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL;





