{
    "query1":"""----------------------- Employees Greater Than Average Salary and Variations 
-- Find all employees whose salary is greater than the average salary of the company
SELECT first_name, last_name,  (SELECT AVG(salary) FROM employees) AS avg_salary FROM EMPLOYEES WHERE salary > (SELECT AVG(SALARY) as s FROM Employees) ; 
-- ****** 
-- Error column "employees.first_name" must appear in the GROUP BY clause or be used in an aggregate function
-- SELECT first_name, last_name, salary,AVG(SALARY)  FROM EMPLOYEES WHERE salary > (SELECT AVG(SALARY) FROM Employees) ; 

WITH avg_salary_cte AS (
    SELECT AVG(salary) AS avg_salary
    FROM employees
)""",
"query2":"""SELECT e.first_name, e.last_name, e.salary, avg_salary_cte.avg_salary
FROM employees e, avg_salary_cte
WHERE e.salary > avg_salary_cte.avg_salary;
-- NOTE : WITH cte is an table as (Statment )  :: Now this is a table can CROSS JOIN with efficiency
-- It can be used anywhere in the code as table, but variable and no cross join
""",
"query3":"""
SELECT e.first_name, e.last_name, e.salary, avg_salary.avg_salary
    FROM employees e
    JOIN (SELECT AVG(salary) AS avg_salary FROM employees) avg_salary
ON e.salary > avg_salary.avg_salary;
"""
"query4":"""
-- Most Effiicient
SET @avg_salary = (SELECT AVG(salary) FROM employees);
SELECT first_name, last_name, salary, @avg_salary AS avg_salary
FROM employees
WHERE salary > @avg_salary;
--------------------------------------------------------------------
"""
}