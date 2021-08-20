-- #1
SELECT 
	e."emp_no", 
	e."first_name",
	e."last_name", 
	e."sex",
	s."emp_no" 
FROM 
	public."Employees" e
	join
	public."Salaries" s on e."emp_no" = s."emp_no";
	
--#2
SELECT
	e."first_name",
	e."last_name",
	e."hire_date"
FROM
	public."Employees" e
WHERE 
	extract(year from e."hire_date") = 1986;
	
--#3 
SELECT
	d."dept_no",
	d."dept_name",
	e."emp_no",
	e."last_name",
	e."first_name"
FROM
	public."Dept_Manager" dm
	join
	public."Departments" d on dm."dept_no" = d."dept_no"
	join
	public."Employees" e on dm."emp_no" = e."emp_no";
	
--#4
SELECT
	e."emp_no",
	e."last_name",
	e."first_name",
	d."dept_name"
FROM
	public."Employees" e
	join
	public."Dept_emp" de on e."emp_no" = de."emp_no"
	join
	public."Departments" d on de."dept_no" = d."dept_no"
	order by emp_no;
	
--#5
SELECT
	--e."emp_no",
	e."first_name",
	e."last_name",
	e."sex"
FROM
	public."Employees" e
WHERE
	e."first_name" = 'Hercules'
AND
	e."last_name" like 'B%';
	
--#6 
SELECT
	e."emp_no",
	e."last_name",
	e."first_name",
	d."dept_name"
FROM
	public."Employees" e
	join
	public."Dept_emp" de on e."emp_no" = de."emp_no"
	join
	public."Departments" d on de."dept_no" = d."dept_no"
WHERE
	d."dept_name" = 'Sales';
	

--#7
SELECT
	e."emp_no",
	e."last_name",
	e."first_name",
	d."dept_name"
FROM
	public."Employees" e
	join
	public."Dept_emp" de on e."emp_no" = de."emp_no"
	join
	public."Departments" d on de."dept_no" = d."dept_no"
WHERE
	d."dept_name" in ('Sales', 'Development');
	
	
--#8
SELECT
	e."last_name",
	count(e."emp_no") AS name_count
FROM
	"Employees" e
GROUP BY
	e."last_name"
order by name_count desc;

