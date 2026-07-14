1_employee_hierarchy.sql

Suppose an employee table exists.

CREATE TABLE employees(
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    manager_id INT
);

Sample data

INSERT INTO employees VALUES
(1,'CEO',NULL),
(2,'Regional Manager',1),
(3,'Branch Manager',2),
(4,'Assistant Manager',3),
(5,'Cashier',4),
(6,'Clerk',4);
Find entire hierarchy
WITH RECURSIVE emp_tree AS
(
    SELECT
        employee_id,
        employee_name,
        manager_id,
        1 AS level

    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        et.level+1

    FROM employees e
    JOIN emp_tree et
    ON e.manager_id=et.employee_id
)

SELECT *
FROM emp_tree
ORDER BY level;
Show reporting path
CEO
   ↓
Regional Manager
   ↓
Branch Manager
   ↓
Assistant Manager
   ↓
Cashier
WITH RECURSIVE hierarchy AS
(
SELECT
employee_id,
employee_name,
manager_id,
employee_name::TEXT path

FROM employees
WHERE manager_id IS NULL

UNION ALL

SELECT
e.employee_id,
e.employee_name,
e.manager_id,
h.path || ' -> ' || e.employee_name

FROM employees e
JOIN hierarchy h
ON e.manager_id=h.employee_id
)

SELECT *
FROM hierarchy;
02_branch_hierarchy.sql

Imagine branches belong to regions.

Head Office

   |

North Region

   |

Mumbai Branch

   |

Mumbai Central

Create table

CREATE TABLE branch_hierarchy
(
branch_id INT PRIMARY KEY,
branch_name VARCHAR(100),
parent_branch INT
);

Sample data

INSERT INTO branch_hierarchy VALUES
(1,'Head Office',NULL),
(2,'North Region',1),
(3,'South Region',1),
(4,'Mumbai Branch',2),
(5,'Delhi Branch',2),
(6,'Chennai Branch',3),
(7,'Bangalore Branch',3);

Recursive query

WITH RECURSIVE branches AS
(
SELECT
branch_id,
branch_name,
parent_branch,
1 level

FROM branch_hierarchy
WHERE parent_branch IS NULL

UNION ALL

SELECT
b.branch_id,
b.branch_name,
b.parent_branch,
br.level+1

FROM branch_hierarchy b
JOIN branches br
ON b.parent_branch=br.branch_id
)

SELECT *
FROM branches;
03_date_series.sql

Very common interview question.

Generate every day of a month.

WITH RECURSIVE dates AS
(
SELECT
DATE '2025-01-01' AS dt

UNION ALL

SELECT
dt+1

FROM dates

WHERE dt<'2025-01-31'
)

SELECT *
FROM dates;

Output

2025-01-01

2025-01-02

2025-01-03

...

2025-01-31

Useful for

Missing transaction dates
Daily dashboards
Time series reports
04_recursive_numbers.sql

Generate numbers.

WITH RECURSIVE numbers AS
(
SELECT 1 n

UNION ALL

SELECT n+1

FROM numbers

WHERE n<100
)

SELECT *
FROM numbers;

Output

1

2

3

...

100
05_recursive_reports.sql

Suppose every branch has child branches.

Calculate total levels.

WITH RECURSIVE branch_tree AS
(
SELECT
branch_id,
branch_name,
parent_branch,
1 depth

FROM branch_hierarchy
WHERE parent_branch IS NULL

UNION ALL

SELECT
b.branch_id,
b.branch_name,
b.parent_branch,
bt.depth+1

FROM branch_hierarchy b
JOIN branch_tree bt
ON b.parent_branch=bt.branch_id
)

SELECT
MAX(depth) AS hierarchy_depth
FROM branch_tree;