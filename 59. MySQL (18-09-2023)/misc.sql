/*
SELECT
It allows us to ectract a fraction of the entire dataset.
ex. SELECT * employees;

SELECT (column_1...) FROM (table_name)
We can specify our source.

ex. select first_name, last_name from employees; names only
*/

# SELECT * FROM employees;



/* 
WHERE
It allows us to set a condition upon which we will specify which part of the
data we want to retrieve.
ex. SELECT... FROM... WHERE (condition)
*/

# select * from employees where first_name = 'Denis';


/*
AND
OR
IN - NOT IN
LIKE - NOT LIKE
BETWEEN... AND...
EXISTS - NOT EXISTS
IS NULL - IS NOT NULL
*/

/*
AND
We can combine two statements.
select (column1...) from (table) where condition1 and condition2
*/
# select * from employees where first_name = 'Denis' and gender='M';


/*
OR
Only one of the conditions has to be met
*/
# select * from employees where first_name = 'Denis' or first_name = 'Mark';

/*
Operator Precedence (logical order)
The operator AND is always applied first, while OR is applied second.
In other words, regardless of the order we use, AND will always be read first.

select * from employees where first_name = 'Denis' AND gender='M' OR gender='F'
would return all male Denis's plus all females!

To fix this we can use parentheses:
select * from employees where first_name = 'Denis' AND (gender='M' OR gender='F')
*/

# select * from employees where (first_name = 'Marco' or first_name = 'Mark') and gender = 'M';



/*
IN - NOT IN
An alternative to repeated OR statements that saves us lots of time.
*/

# instead of this > ...where first_name = 'Mark' or first_name = 'Marco' or first_name = 'Nathan'
# select * from employees where first_name IN ('Mark','Marco','Nathan')

# NOT IN will exclude our input
# select * from employees where first_name NOT IN ('Mark','Marco','Nathan');



/*
LIKE - NOT LIKE
We state a pattern with % and _ signs.
% > sequence
_ > single character

MySQL is case insensitive.
*/

# select * from employees where first_name LIKE ('Mar%');
# our pattern will be all names that start with 'mar'

# We can also move the % sign
# select * from employees where last_name LIKE ('%man%');

# select * from employees where first_name LIKE ('Mar_');
# this will select all names starting with 'mar' and with 4 letters only


/*
Wildcard Characters > % _ *
* can also be used to call all rows of a table.
*/


/*
(NOT) BETWEEN... AND...
Helps us designate the interval to which a given value belongs.
*/

# select * from employees where hire_date BETWEEN '1990-01-01' AND '2000-01-01'; # both values included!

# select * from employees where hire_date NOT BETWEEN '1990-01-01' AND '2000-01-01'; # in this case both values are NOT included.



/*
IS (NOT) NULL
We excract values that are (not) null.
*/

# select * from employees where first_name IS NULL; no names missing


/*
Comparison operators:    =	>	<	>=	<=	!=
*/
# select * from employees where (hire_date >= '1999-01-01' and hire_date < '2000-01-01');



/*
SELECT DISTINCT
Allows us to retrieve all distinc, different data values
*/

# SELECT DISTINCT gender from employees;



/*
Aggregate Functions
They are applied to multiple rows of a single column and return an output of a single value.

COUNT()
Returns the number of all non-null records within a field

SUM()
Returns the sum of all non-null  values.

MIN()/MAX()
Returns the min/max value of the entire list.

AVG()
*/

# select COUNT('emp_no') from employees; # we have 300024 employees

# How many distinc names?
# select COUNT(DISTINCT first_name) from employees; # 1275 different given names

# How many annual contracts with a value higher than or equal to $100,000 have been registered in the salaries table?
# select COUNT(salary) from salaries where salary >= '100000'; #32207


/*
ORDER BY (+ ASC / DESC)
We can use it to order the list by a specific parameter.
*/

# select * from employees ORDER BY birth_date DESC;



/*
GROUP BY
In most cases, when you use an aggreagte function, you must add a GROUP BY query too

ex. slect... from... [where (conditions)] GROUP BY (column names) [order by ...]
*/

# select COUNT(first_name) from employees GROUP BY first_name; 
# with this we see how many times we encounter the name, but not the name itself...

# select first_name, COUNT(first_name) from employees GROUP BY first_name order by first_name; 

/*
We can edit the columns names (the standard would be the function key name.
*/
# select first_name, COUNT(first_name) as name_count from employees GROUP BY first_name order by first_name; 



/*
HAVING
Refines the output from records that do not satisfy a certain condition.
It is frequently accompanied by ORDER BY.
You CANNOT have having count(column) + column [>] condition
WHERE goes before HAVING
*/

# select * from employees where hire_date >= '2000-01-01';
# same as
# select * from employees HAVING hire_date >= '2000-01-01';
# but WHERE cannot be followed by aggregate functions

# select first_name,COUNT(first_name) as name_count from employees where COUNT(first_name) > 250 group by first_name order by first_name;
# This returns an error, albeit with correct syntax
# select first_name,COUNT(first_name) as name_count from employees group by first_name HAVING COUNT(first_name) > 250  order by first_name;
# remember to change the syntax order


/*
# retrieve all employees whose name count > 200 and limit the data to hire dates > 1999-01-o1
select first_name,count(first_name) as name_count from employees 
# we then use WHERE because the condition refers to single rows in the employees table
where  hire_date > '1980-01-01' 
# then because we have an aggregate function we use having
group by first_name
having count(first_name) > 200
order by first_name desc;
*/


/*
Select the employee numbers of all individuals who have signed more than 1 contract after the 1st of January 2000.
select emp_no, count(emp_no) as emp_count from dept_emp
where from_date > '2000-01-01'
group by emp_no
having count(dept_no) > 1;
*/



/*
LIMIT
*/

# Show the 10 highest paid employees
select * from salaries order by salary desc LIMIT 10;