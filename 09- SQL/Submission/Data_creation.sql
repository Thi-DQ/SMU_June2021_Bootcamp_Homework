-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Departments" (
    "dept_no" varchar(5)   NOT NULL,
    "dept_name" varchar(30)   NOT NULL,
    "last_updated" timestamp default localtimestamp  NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "Dept_emp" (
    "id" serial   NOT NULL,
    "emp_no" integer   NOT NULL,
    "dept_no" varchar(30)   NOT NULL,
    "last_updated" timestamp default localtimestamp  NOT NULL,
    CONSTRAINT "pk_Dept_emp" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Dept_Manager" (
    "id" serial   NOT NULL,
    "dept_no" varchar(10)   NOT NULL,
    "emp_no" integer   NOT NULL,
    "last_updated" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_Dept_Manager" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Employees" (
    "id" serial   NOT NULL,
    "emp_no" integer   NOT NULL,
    "emp_title" varchar(30)   NOT NULL,
    "birth_date" timestamp   NOT NULL,
    "first_name" varchar(30)   NOT NULL,
    "last_name" varchar(30)   NOT NULL,
    "sex" varchar(30)   NOT NULL,
    "hire_date" timestamp   NOT NULL,
    "last_updated" timestamp default localtimestamp  NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Salaries" (
    "id" serial   NOT NULL,
    "emp_no" integer   NOT NULL,
    "salary" integer   NOT NULL,
    "last_updated" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Titles" (
    "id" serial   NOT NULL,
    "title_id" varchar(5)   NOT NULL,
    "title" varchar(30)   NOT NULL,
    "last_updated" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "Departments" ADD CONSTRAINT "fk_Departments_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Dept_emp" ("dept_no");

ALTER TABLE "Dept_emp" ADD CONSTRAINT "fk_Dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Dept_Manager" ADD CONSTRAINT "fk_Dept_Manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "Dept_Manager" ADD CONSTRAINT "fk_Dept_Manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Employees" ADD CONSTRAINT "fk_Employees_emp_title" FOREIGN KEY("emp_title")
REFERENCES "Titles" ("title_id");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");
