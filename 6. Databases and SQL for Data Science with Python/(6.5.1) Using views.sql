-- How does the syntax of a CREATE VIEW statement look?
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- How does the syntax of a REPLACE VIEW statement look?
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- How does the syntax of a DROP VIEW statement look?
DROP VIEW view_name;

-- Exercise 1: Create a View

/* 1. Let’s create a view called EMPSALARY to display salary along with some basic sensitive data of employees from the HR database. 
To create the EMPSALARY view from the EMPLOYEES table. Click Go. */
CREATE VIEW EMPSALARY AS 
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, SALARY
FROM EMPLOYEES; 

/* 2. Using SELECT, query the EMPSALARY view to retrieve all the records. Click Go. */
SELECT * FROM EMPSALARY;

-- Exercise 2: Update a View

/* 1. It now seems that the EMPSALARY view we created in exercise 1 doesn’t contain enough salary information, such as max/min salary 
and the job title of the employees. Let’s update the EMPSALARY view:
	- combining two tables EMPLOYEES and JOBS so that we can display our desired information from the HR database.
	- including the columns JOB_TITLE, MIN_SALARY, MAX_SALARY of the JOBS table as well as excluding the SALARY 
	  column of the EMPLOYEES table. */
CREATE OR REPLACE VIEW EMPSALARY  AS 
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE, MIN_SALARY, MAX_SALARY
FROM EMPLOYEES, JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;

/* 2. Using SELECT, query the updated EMPSALARY view to retrieve all the records. Click Go. */
SELECT * FROM EMPSALARY;

-- Exercise 3: Drop a View

/* 1. Let’s delete the created EMPSALARY view. Click Go. */
DROP VIEW EMPSALARY;

/* 2. Using SELECT, you can verify whether the EMPSALARY view has been deleted or not. Click Go. */
SELECT * FROM EMPSALARY;