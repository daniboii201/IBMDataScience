-- How does a CROSS JOIN (also known as Cartesian Join) statement syntax look?
SELECT column_name(s)
FROM table1
CROSS JOIN table2;

-- How does an INNER JOIN statement syntax look?
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
WHERE condition;

-- How does a LEFT OUTER JOIN statement syntax look?
SELECT column_name(s)
FROM table1
LEFT OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;

-- How does a RIGHT OUTER JOIN statement syntax look?
SELECT column_name(s)
FROM table1
RIGHT OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;

-- How does a FULL OUTER JOIN statement syntax look?
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;

-- How does a SELF JOIN statement syntax look?
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;

-- Exercise

/* Select the names and job start dates of all employees who work for the department number 5. */
select E.F_NAME,E.L_NAME, JH.START_DATE 
from EMPLOYEES as E 
INNER JOIN JOB_HISTORY as JH on E.EMP_ID=JH.EMPL_ID 
where E.DEP_ID ='5';

/* Select the names, job start dates, and job titles of all employees who work for the department number 5. */
select E.F_NAME, E.L_NAME, 	JH.START_DATE, J.JOB_TITLE
from EMPLOYEES as E
INNER JOIN JOB_HISTORY as JH on E.EMP_ID=JH.EMPL_ID 
INNER JOIN JOBS as J on E.JOB_ID=J.JOB_IDENT
where E.DEP_ID ='5'; 

/* Perform a Left Outer Join on the EMPLOYEES and DEPARTMENT tables and select employee id, last name, department id and 
department name for all employees. */
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEPT_ID_DEP
from EMPLOYEES as E
LEFT OUTER JOIN DEPARTMENTS as D on E.DEP_ID = DEPA.DEPT_ID_DEP;

/* Re-write the previous query but limit the result set to include only the rows for employees born before 1980. */
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEPT_ID_DEP, E.B_DATE
from EMPLOYEES as E
LEFT OUTER JOIN DEPARTMENTS as D on E.DEP_ID = D.DEPT_ID_DEP
where YEAR(E.B_DATE) < 1980;

/* Re-write the previous query but have the result set include all the employees but department names for only the employees 
who were born before 1980. */
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEPT_ID_DEP, E.B_DATE
from EMPLOYEES as E
LEFT OUTER JOIN DEPARTMENTS as D on E.DEP_ID = D.DEPT_ID_DEP
and YEAR(E.B_DATE) < 1980;

/* Perform a Full Join on the EMPLOYEES and DEPARTMENT tables and select the First name, Last name and Department 
name of all employees. */ 
select E.F_NAME, E.L_NAME, D.DEP_NAME
from EMPLOYEES as E
FULL OUTER JOIN DEPARTMENTS as D on E.DEP_ID = D.DEPT_ID_DEP;

/* Re-write the previous query but have the result set include all employee names but department id and 
department names only for male employees. */
select E.F_NAME, E.L_NAME, D.DEP_NAME
from EMPLOYEES as E
FULL OUTER JOIN DEPARTMENTS as D on E.DEP_ID = D.DEPT_ID_DEP
and E.SEX = 'M';