# SQL and Relational Databases

SQL fundamentals, relational design, indexing, transactions, query patterns, and exercises.

[Back to the question-bank index](../README.md)

## What is a stored procedure?

**Answer**

A stored procedure is a named routine stored in the database and invoked by a client or another
routine. It can group SQL and procedural statements, accept parameters, manage database-side logic,
and return output parameters or result sets depending on the database.

Procedures can reduce round trips and keep data-intensive work close to the data, and permissions can
be granted on a procedure without granting direct access to every underlying table. They also create
vendor-specific code and deployment, testing, observability, and versioning responsibilities.
"Precompiled and therefore faster" is not a universal guarantee; plan caching and execution behavior
are database-specific.

## What is the difference between Function and Stored Procedure?

**Answer**

The exact distinction is vendor-specific. Generally, a function returns a value and may be usable
inside a query expression, while a procedure is invoked as a statement and may expose result sets,
output parameters, transaction control, or broader side effects.

Do not rely on blanket rules such as "functions cannot modify data" or "functions are faster":
Oracle, PostgreSQL, SQL Server, and MySQL impose different restrictions and invocation syntax. Answer
for the database named by the interviewer and discuss purity, transaction behavior, and optimizer
visibility for that engine.

## What is Normalization?

**Answer**

Normalization is a database design technique used to reduce redundancy and improve data integrity by organizing tables into smaller, related tables and defining relationships between them. The process involves achieving various normal forms, each with specific criteria to ensure efficient and consistent data storage.
- **1NF:** each row-column intersection contains one value from its domain and rows are identifiable.
- **2NF:** it is in 1NF and every non-key attribute depends on the whole candidate key, not part of a
  composite key.
- **3NF:** it is in 2NF and non-key attributes do not depend transitively on a key.
- **BCNF:** every non-trivial functional dependency has a determinant that is a superkey.

Normalization improves integrity and reduces update anomalies. Deliberate denormalization can improve
specific read paths, but it adds synchronization responsibilities and should follow measured need.

## How do you model a one-to-many relationship with a foreign key?

**Answer**

Place the primary key from the "one" table as a foreign key in the "many" table. For example, one
department can have many employees, while each employee belongs to one department:

```sql
CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    department_id INTEGER NOT NULL,
    employee_name VARCHAR(100) NOT NULL,
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id) REFERENCES department (department_id)
);
```

Indexing the foreign-key column is often useful for joins and parent-row changes, but exact index
requirements depend on the database and workload.

## How would you store notifications?

**Answer**

Store one notification entity with fields such as `notification_id`, type, immutable payload or
template inputs, creation time, and expiry. Model recipient state separately when one notification
can target many users:

- `notification(notification_id, type, payload, created_at, expires_at)`
- `user_notification(user_id, notification_id, read_at, delivery_status)`

Index for the actual retrieval pattern, for example `(user_id, read_at, notification_id)` for a
user's unread feed. Define retention, pagination, fan-out strategy, idempotent delivery, and whether
read state must synchronize across devices.

## How does notification volume affect the storage design?

**Answer**

Start with measured cardinality and access patterns: users, notifications per user per day, retention,
read/write ratio, fan-out size, payload size, and latency target. Estimate rows and storage before
choosing sharding.

Use indexes and keyset pagination first. Time-based partitioning can help retention and maintenance at
large scale. A queue can decouple delivery workers, and a cache can accelerate a bounded hot feed,
but neither replaces durable state. Shard only when one database can no longer meet the measured
capacity or isolation requirement, because cross-shard queries and rebalancing add complexity.

## How can you optimize your database queries?

**Answer**

1. Capture the slow statement with representative parameter values and measure latency, rows, calls,
   waits, and resource use.
2. Inspect the actual execution plan and cardinality estimates. Look for excessive scans, bad join
   choices, spills, repeated lookups, sorts, lock waits, or rows multiplied unexpectedly.
3. Return only needed rows and columns, paginate with a stable order, and remove unnecessary joins or
   repeated queries.
4. Add or adjust selective indexes whose leading columns match filters and joins and whose order can
   support sorting. Account for write and storage cost.
5. Keep predicates sargable where possible and use correct data types and statistics.
6. Batch work carefully and shorten transactions. Consider partitioning, caching, precomputation, or
   schema changes only for a demonstrated bottleneck.
7. Re-measure under realistic concurrency and verify that other important queries did not regress.

Subqueries are not inherently slower than joins; a modern optimizer may transform either form. Tune
the plan and semantics, not syntax folklore.

## Explain Patterns to Optimize DB (Indexing, Partitioning, Sharding, etc)

**Answer**

- **Indexing** adds an access structure inside a database to avoid or reduce scanning for particular
  predicates, joins, and orders. It costs storage and write maintenance.
- **Partitioning** divides one logical table or index into managed pieces, often by range, list, or
  hash. It helps pruning and lifecycle operations only when queries align with the partition key.
- **Sharding** distributes data across independent database nodes. It can expand capacity and isolate
  tenants but complicates routing, joins, uniqueness, transactions, and rebalancing.

Also consider query and schema correction, statistics, batching, read replicas, materialized views,
and caching. Choose the smallest mechanism that addresses measured limits.

## How to achieve Atomicity during a Transaction

**Answer**

Group all required database changes in one transaction. Commit only after every invariant is
satisfied; on failure, roll back. The database uses its transaction and recovery mechanisms to make
the committed outcome durable and uncommitted partial work invisible according to the isolation
level.

For multiple resource managers, two-phase commit can coordinate an atomic outcome only when all
participants support the protocol, and it carries availability and operational costs. Application-
level compensation or a saga is not atomic rollback; it is a different consistency model. Prefer a
single transactional boundary or patterns such as a transactional outbox where possible.

## If a table is frequently updated what type of index should we use on that?

**Answer**

There is no universally best index type for an update-heavy table. Every affected index adds work to
inserts, deletes, and updates, especially when indexed key values change.

Keep only indexes justified by important read paths. Prefer narrow, selective keys with stable values;
use a composite or covering index only when its column order matches a real query. A filtered or
partial index can reduce maintenance when a frequently queried subset is small. Clustered-index and
heap behavior is database-specific. Confirm the choice with actual plans and write-load tests.

## What is a balanced index?

**Answer**

A balanced-tree index keeps leaf pages at approximately the same depth, so point lookups, inserts,
deletes, and ordered range scans have predictable logarithmic traversal cost. Database engines
commonly use B-tree-family structures; implementation details such as whether values appear only in
leaf pages vary by engine.

Balance does not mean every page is full. Page splits, merges, fill factors, and background
maintenance trade space utilization against write cost. Hash, bitmap, inverted, and spatial indexes
serve different access patterns, so a balanced-tree index is not automatically the best choice.

## Find the 3rd Highest Salary in Employee Table?

**Answer**

```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
```

This syntax is supported by databases such as PostgreSQL and MySQL. It returns the third distinct
salary, not necessarily one employee. A `DENSE_RANK` solution is more portable when ties must be
explicitly represented.

## How do you calculate total salary by gender?

**Answer**

```sql
SELECT gender, SUM(salary) AS total_salary
FROM Employee
GROUP BY gender;
```

## How do you return passengers who have an assigned seat?

**Answer**

```sql
SELECT p.passenger_id, p.passenger_name, s.seat_number
FROM Passengers p
INNER JOIN Seats s ON p.passenger_id = s.passenger_id;
```

## How do you identify duplicate records in a table?

**Answer**

```sql
SELECT column1, column2, COUNT(*)
FROM your_table
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```

## How can you delete duplicate records from a table?

**Answer**

```sql
WITH CTE AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY column1, column2 ORDER BY (SELECT NULL)) AS row_num
    FROM your_table
)
DELETE FROM CTE
WHERE row_num > 1;
```

This form works in SQL Server when the common table expression is updatable. Replace the
nondeterministic `ORDER BY (SELECT NULL)` with a stable key that identifies which row should be kept.
For other databases, delete by primary key using a subquery and verify the candidates in a
transaction before deleting.

## What's the difference between UNION and UNION ALL?

**Answer**

`UNION` combines compatible result sets and removes duplicate rows. `UNION ALL` retains every row
and is generally cheaper because it does not perform duplicate elimination. Corresponding columns
must have compatible types, and the final column names come from the first query.

```sql
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;

SELECT column1, column2 FROM table1
UNION ALL
SELECT column1, column2 FROM table2;
```

Use `UNION ALL` unless the result specifically requires set semantics.

## How do RANK, ROW_NUMBER, and DENSE_RANK differ?

**Answer**

All three are window functions whose numbering restarts for each optional partition:

- `ROW_NUMBER` assigns a unique sequence even when ordering values tie.
- `RANK` gives tied rows the same rank and leaves gaps afterward, such as `1, 1, 3`.
- `DENSE_RANK` gives tied rows the same rank without gaps, such as `1, 1, 2`.

```sql
SELECT column1, column2,
       ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2) AS row_num
FROM your_table;

SELECT column1, column2,
       RANK() OVER (PARTITION BY column1 ORDER BY column2) AS rank
FROM your_table;

SELECT column1, column2,
       DENSE_RANK() OVER (PARTITION BY column1 ORDER BY column2) AS dense_rank
FROM your_table;
```

Add a unique tiebreaker to the window `ORDER BY` when `ROW_NUMBER` must be deterministic.

## How do you find records in one table that don’t exist in another?

**Answer**

Three common anti-join forms are:

```sql
SELECT a.*
FROM table1 a
LEFT JOIN table2 b ON a.common_column = b.common_column
WHERE b.common_column IS NULL;

SELECT *
FROM table1
WHERE common_column NOT IN (SELECT common_column FROM table2);

SELECT *
FROM table1 a
WHERE NOT EXISTS (
    SELECT 1
    FROM table2 b
    WHERE a.common_column = b.common_column
);
```

`NOT EXISTS` is usually the safest expression of the intent. `NOT IN` can return no rows when its
subquery contains `NULL`, unless nulls are excluded explicitly. With a left anti-join, test a
non-nullable column from the right table.

## How can you retrieve the second-highest salary for employees in each department?

**Answer**

```sql
SELECT department, salary
FROM (
    SELECT department, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
) ranked_salaries
WHERE rank = 2;
```

## How do you find employees earning more than their manager?

**Answer**

```sql
SELECT e.employee_id, e.employee_name, e.salary, m.employee_name AS manager_name, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;
```

## What's the difference between INNER JOIN and LEFT JOIN?

**Answer**

An `INNER JOIN` returns only matching row combinations. A `LEFT JOIN` returns every left-side row;
when no right-side row matches, right-side columns are `NULL`. Duplicate matching keys can multiply
rows in either form.

```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.common_column = table2.common_column;

SELECT columns
FROM table1
LEFT JOIN table2 ON table1.common_column = table2.common_column;
```

A filter on a right-side column in the `WHERE` clause can unintentionally make a left join behave
like an inner join. Put match-specific predicates in the `ON` clause when unmatched left rows must
remain.

## What is the difference between DROP, DELETE and TRUNCATE?

**Answer**

- `DELETE` removes selected rows and retains the table. It supports a `WHERE` clause.
- `TRUNCATE` removes all rows while retaining the table definition. It is usually optimized as a
  bulk operation and often has restrictions involving foreign keys, identity state, or triggers.
- `DROP` removes the database object itself, including its data and definition.

Transaction, logging, trigger, permission, and rollback behavior varies by database. For example,
SQL Server and PostgreSQL can roll back many `TRUNCATE` and `DROP` operations inside a transaction,
while some engines implicitly commit DDL. State the target engine rather than memorizing a universal
rollback rule.

```sql
DROP TABLE Employees;
DELETE FROM Employees WHERE employee_id = 1;
TRUNCATE TABLE Employees;
```

## How would you update a table to swap gender values?

**Answer**

```sql
UPDATE your_table
SET gender = CASE
    WHEN gender = 'Male' THEN 'Female'
    WHEN gender = 'Female' THEN 'Male'
    ELSE gender
END;
```

## How do you create a DB and Table in SQL?

**Answer**

```sql
-- SQL Server / MySQL-style example; database selection syntax is vendor-specific.
CREATE DATABASE CompanyDB;
USE CompanyDB;

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    salary DECIMAL(10, 2)
);
```

Database creation and selection are not portable SQL. For example, PostgreSQL connects to the
created database rather than supporting `USE`.

## How do you calculate product revenue by date in a warehouse schema?

**Answer**

```sql
SELECT
    p.product_name,
    d.date,
    SUM(o.revenue) AS total_revenue
FROM
    orders o
JOIN
    products p ON o.product_id = p.product_id
JOIN
    customers c ON o.customer_id = c.customer_id
JOIN
    dates d ON o.date_id = d.date_id
GROUP BY
    p.product_name, d.date
ORDER BY
    p.product_name, d.date;
```

The customer join is unnecessary unless the query filters or groups by a customer attribute. Remove
unused joins to avoid accidental row multiplication and needless work.

## How do you calculate the average category ID for each category type?

**Answer**

```sql
SELECT type, AVG(id) AS average_id
FROM categories
GROUP BY type;
```

## Find the count of employees in each city?

**Answer**

```sql
SELECT city, COUNT(*) AS employee_count
FROM Employees
GROUP BY city;
```

## What is COMMIT & ROLLBACK?

**Answer**

`COMMIT` completes the current transaction and makes its changes durable. When those changes become
visible to other transactions depends on their isolation level and snapshots.

`ROLLBACK` aborts the current transaction and reverses its uncommitted database changes. It cannot
undo a transaction that has already committed, and external side effects such as an email or an
ordinary HTTP request are not automatically reversed.

```sql
COMMIT;
ROLLBACK;
```

## Number of records after different kinds of join?

**Answer**

Join type alone does not determine an exact row count. For each join-key value, an inner join emits
the product of matching rows from the two inputs. Therefore, two left rows and three right rows with
the same key produce six rows.

- `INNER JOIN` emits only matched combinations.
- `LEFT JOIN` also emits one null-extended row for each unmatched left row.
- `RIGHT JOIN` does the symmetric operation for unmatched right rows.
- `FULL OUTER JOIN` emits matched combinations plus null-extended rows from both unmatched sides.

A full outer join does not automatically return the number of unique input rows. Use key constraints
and the frequency of each matching key to calculate cardinality.

## Which toys were requested by children under nine years old?

**Answer**

Given `Children(child_name, age)`, `Toys(toy_name, price)`, and
`RequestedToy(child_name, toy_name)`:

```sql
SELECT t.toy_name
FROM RequestedToy l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name
WHERE c.age < 9
ORDER BY t.toy_name;
```

Add `DISTINCT` if each toy should appear only once rather than once per request.

## What is the total amount spent by each child?

**Answer**

```sql
SELECT c.child_name, SUM(t.price) AS total_amount_spent
FROM RequestedToy l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name
GROUP BY c.child_name;
```

## Who are the children spending over 200?

**Answer**

```sql
SELECT c.child_name, SUM(t.price) AS total_amount_spent
FROM RequestedToy l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name
GROUP BY c.child_name
HAVING SUM(t.price) > 200;
```

## What are Database views?

**Answer**

A view is a named query that exposes a table-like interface over one or more relations. A regular view
usually stores its definition rather than a separate copy of its result. It can simplify repeated
queries, provide a stable abstraction over schema details, and restrict exposed rows or columns when
combined with appropriate permissions.

Whether a view is updatable depends on its definition and the database. Aggregates, grouping, set
operations, and some joins commonly make direct updates impossible. A materialized view is different:
it stores query results and must be refreshed according to database-specific rules.

```sql
CREATE VIEW active_employees AS
SELECT employee_id, employee_name, department_id
FROM Employees
WHERE status = 'ACTIVE';
```
