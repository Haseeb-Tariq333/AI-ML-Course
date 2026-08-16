CREATE DATABASE COMPANY;
USE COMPANY;

CREATE TABLE Employees(
EMPID INT PRIMARY KEY,
FirstName VARCHAR(30) NOT NULL,
LastName Varchar(30),
Department VARCHAR(50),
SALARY INT,
HireDate DATE
);

INSERT INTO Employees (EMPID, FirstName, LastName, Department, SALARY, HireDate) VALUES 
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-3-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-7-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');


SELECT * FROM EMPLOYEES;

SELECT FirstName, LastName, SALARY FROM EMPLOYEES;

SELECT * FROM EMPLOYEES WHERE Department = 'IT';

SELECT * FROM EMPLOYEES WHERE SALARY > 6000;

SELECT * FROM EMPLOYEES ORDER BY HireDate DESC;

SELECT AVG(SALARY) FROM EMPLOYEES;

SELECT * FROM EMPLOYEES WHERE SALARY BETWEEN 4000 AND 7000;

SELECT DISTINCT Department FROM EmployeeS;

SELECT * FROM EmployeeS WHERE FirstName LIKE 'A%';

SELECT Department, COUNT(EmpID) AS NumberOfEmployees
FROM EmployeeS
GROUP BY Department
HAVING COUNT(EmpID) > 3;
