# SQL and Relational Databases

SQL fundamentals, relational design, indexing, transactions, query patterns, and exercises.

[Back to the question-bank index](../README.md)

## What is a Stored Procedure

**Answer**

Stored Procedure is a precompiled set of one or more SQL statements that are stored in the database. They can be executed as a single unit, allowing for more efficient and secure database operations.
Pros:
Performance: Stored procedures are precompiled, which can lead to faster execution times compared to executing individual SQL statements.
Reduced Network Traffic: By executing multiple SQL statements in a single call, stored procedures reduce the amount of data sent between the application and the database server.
Cons:
Vendor Lock-In: Each database vendor has its own language for stored procedures (e.g., PL/SQL for Oracle, T-SQL for SQL Server), making it difficult to migrate to a different database system.
Version Control: Managing stored procedures in version control systems can be awkward compared to application code.

## What is the difference between Function and Stored Procedure?

**Answer**

Return Type:
Function: Must return a value (scalar or table).
Stored Procedure: Can return zero or more result sets and output parameters.
Usage in SQL Statements:
Function: Can be used in SQL statements like SELECT, WHERE, JOIN.
Stored Procedure: Cannot be used directly in SQL statements; must be executed with EXEC or CALL.
Database State Modification:
Function: Cannot modify the database state.
Stored Procedure: Can modify the database state.
Error Handling:
Function: Limited error handling capabilities.
Stored Procedure: More robust error handling with TRY...CATCH blocks.
Performance:
Function: Generally faster for computations and data transformations.
Stored Procedure: Suitable for complex operations and batch processing.

## What is Normalization?

**Answer**

Normalization is a database design technique used to reduce redundancy and improve data integrity by organizing tables into smaller, related tables and defining relationships between them. The process involves achieving various normal forms, each with specific criteria to ensure efficient and consistent data storage.
First Normal Form (1NF): Ensure atomic values and single data type per column.
Second Normal Form (2NF): Remove partial dependencies.
Third Normal Form (3NF): Remove transitive dependencies.
Boyce-Codd Normal Form (BCNF): Ensure that every determinant is a candidate key.

Model a simple one-to-many relationship using foreign key
To model a simple one-to-many relationship using a foreign key in a relational database, you need to create two tables: one representing the "one" side of the relationship and the other representing the "many" side. The table on the "many" side will have a foreign key that references the primary key of the table on the "one" side.
One-to-Many Relationship Between Department and Employee
In this example, each department can have multiple employees, but each employee belongs to exactly one department.

## How would you store notifications?

**Answer**

Storing Notifications
Notifications Table: Store notifications with fields for notificationId, userId, message, timestamp, and isRead.
Indexing: Index the userId field to quickly retrieve notifications for a specific user.

## How many users and notifications?

**Answer**

Scalability Considerations
Users and Notifications: Use sharding and partitioning to distribute the load across multiple servers.
High Throughput: Implement caching for frequently accessed data and use message queues for handling high volumes of notifications.

## How can you optimize your database queries?

**Answer**

Indexing:
Create indexes on columns that are frequently used in WHERE, JOIN, ORDER BY, and GROUP BY clauses.
Avoid over-indexing, as it can slow down INSERT, UPDATE, and DELETE operations.
CREATE INDEX idx_column_name ON table_name(column_name);
Use Appropriate Data Types:
Choose the most efficient data type for each column to save space and improve performance.
Avoid SELECT:
Select only the columns you need to reduce the amount of data transferred.
SELECT column1, column2 FROM table_name;
Use Joins Efficiently:
Use INNER JOIN instead of LEFT JOIN if you don't need unmatched rows.
Ensure that join columns are indexed.
Optimize WHERE Clauses:
Use indexed columns in WHERE clauses.
Avoid functions on columns in WHERE clauses, as they can prevent the use of indexes.
SELECT * FROM table_name WHERE column_name = 'value';
Limit the Result Set:
Use LIMIT or TOP to restrict the number of rows returned.
SELECT column1, column2 FROM table_name LIMIT 10;
Use EXPLAIN:
Use the EXPLAIN statement to analyze query execution plans and identify bottlenecks.

EXPLAIN SELECT column1, column2 FROM table_name WHERE column_name = 'value';
Avoid Subqueries:
Use joins instead of subqueries where possible, as joins are often more efficient.
SELECT a.column1, b.column2
FROM table1 a
JOIN table2 b ON a.id = b.id;
Batch Updates and Inserts:
Perform bulk inserts and updates in batches to reduce transaction overhead.
Use Caching:
Cache frequently accessed data to reduce the load on the database.
Partitioning:
Partition large tables to improve query performance and manageability.
Database Configuration:
Optimize database configuration settings (e.g., buffer pool size, cache size) based on your workload.

## Explain Patterns to Optimize DB (Indexing, Partitioning, Sharding, etc)

**Answer**

Indexing: Improves query performance by creating indexes on columns.
Partitioning: Divides large tables into smaller partitions for better manageability and performance.
Sharding: Splits a large database into smaller shards for improved scalability and performance.

## How to achieve Atomicity during a Transaction

**Answer**

Atomicity: Ensures that a series of operations within a transaction are treated as a single unit, which either fully completes or fully fails.
Transaction: A sequence of operations performed as a single logical unit of work.
Commit: Finalizes a transaction, making all changes permanent.
Rollback: Undoes all changes made during a transaction if any operation fails.
Using Database Transactions: Group multiple operations into a single transaction using SQL or other database-specific transaction mechanisms.
Using Two-Phase Commit (2PC): Ensures atomicity in distributed systems through a two-phase protocol.
Using Application-Level Transactions: Implement custom transaction management logic at the application level for databases that do not natively support transactions.

## If a table is frequently updated what type of index should we use on that?

**Answer**

For a table that is frequently updated, a non-clustered index or a filtered index is generally the best choice.
Clustered Index:
Determines the physical order of data in the table.
Suitable for range queries and sorted results.

**Can lead to fragmentation and maintenance overhead during frequent updates.**

Non-Clustered Index:
Creates a separate structure to store the index.
Suitable for frequently queried columns.
Balances read performance and maintenance overhead.
Covering Index:
Includes all columns needed to satisfy a query.
Reduces the need to access table data.

**Can become large and require more maintenance.**

Filtered Index:
Includes only a subset of rows based on a filter condition.
Reduces maintenance overhead for updates that do not affect the filtered subset.
Suitable for indexing frequently queried subsets of data.
Composite Index:
Includes multiple columns in the index key.
Improves performance of queries that filter or sort by multiple columns.

**Can be complex to maintain and may not be as effective if query patterns change.**

## What is a balanced index?

**Answer**

Balanced Index:
An index that maintains a balanced tree structure to ensure efficient search, insert, and delete operations.
Common types include B-trees and B+ trees.
Key Characteristics:
Balanced tree structure.
Efficient search, insert, and delete operations.
Minimized disk I/O.
Common Types:
B-tree: Self-balancing tree with multiple children per node.
B+ tree: Variant of B-tree with all data in leaf nodes and linked leaf nodes for efficient range queries.
Advantages:
Efficient query performance.
Scalability.
Support for range queries.
Minimized disk I/O.
Use Cases:
Database indexing.
File systems.
Search engines.

## Find the 3rd Highest Salary in Employee Table?

**Answer**

```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
Write a query to print total salaries of Male and Female Employees from an Employee Table
SELECT gender, SUM(salary) AS total_salary
FROM Employee
GROUP BY gender;
Write a query to fetch all the Passengers that have a seat assigned from Passengers and Seats Table
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
```

WHERE row_num > 1;
## What's the difference between UNION and UNION ALL?

**Answer**

UNION:
Combines the result sets of two or more SELECT statements.
Removes duplicate rows from the result set.
Syntax:
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;
UNION ALL:
Combines the result sets of two or more SELECT statements.
Includes all duplicate rows in the result set.
Syntax:
SELECT column1, column2 FROM table1
UNION ALL
SELECT column1, column2 FROM table2;

## How do RANK, ROW_NUMBER, and DENSE_RANK differ?

**Answer**

ROW_NUMBER:
Assigns a unique sequential integer to rows within a partition, starting at 1.
No gaps in the sequence.
Syntax:
SELECT column1, column2,
       ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2) AS row_num
FROM your_table;
RANK:
Assigns a rank to each row within a partition, starting at 1.
Rows with the same values receive the same rank, and the next rank is incremented by the number of duplicate ranks.

**Can have gaps in the sequence.**

Syntax:
SELECT column1, column2,
       RANK() OVER (PARTITION BY column1 ORDER BY column2) AS rank
FROM your_table;
DENSE_RANK:
Similar to RANK, but without gaps in the ranking sequence.
Rows with the same values receive the same rank, and the next rank is incremented by 1.
Syntax:
SELECT column1, column2,
       DENSE_RANK() OVER (PARTITION BY column1 ORDER BY column2) AS dense_rank
FROM your_table;

## How do you find records in one table that don’t exist in another?

**Answer**

Using LEFT JOIN and WHERE:
SELECT a.*
FROM table1 a
LEFT JOIN table2 b ON a.common_column = b.common_column

WHERE b.common_column IS NULL;
Using NOT IN:
SELECT *
FROM table1

WHERE common_column NOT IN (SELECT common_column FROM table2);
Using NOT EXISTS:
SELECT *
FROM table1 a

WHERE NOT EXISTS (
    SELECT 1
    FROM table2 b
    WHERE a.common_column = b.common_column
);

## How can you retrieve the second-highest salary for employees in each department?

**Answer**

```sql
SELECT department, salary
FROM (
    SELECT department, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
) ranked_salaries
```

WHERE rank = 2;
## How do you find employees earning more than their manager?

**Answer**

```sql
SELECT e.employee_id, e.employee_name, e.salary, m.employee_name AS manager_name, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
```

WHERE e.salary > m.salary;
## What's the difference between INNER JOIN and LEFT JOIN?

**Answer**

INNER JOIN:
Returns only the rows that have matching values in both tables.
If there is no match, the row is not included in the result set.
Syntax:
SELECT columns
FROM table1
INNER JOIN table2 ON table1.common_column = table2.common_column;
LEFT JOIN (or LEFT OUTER JOIN):
Returns all rows from the left table, and the matched rows from the right table.
If there is no match, the result is NULL on the side of the right table.
Syntax:
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.common_column = table2.common_column;

## What is the difference between DROP, DELETE and TRUNCATE?

**Answer**

Scope:
DROP: Removes the entire table (or other database objects).
DELETE: Removes specific rows based on a condition.
TRUNCATE: Removes all rows from a table.
Rollback:
DROP: Cannot be rolled back.
DELETE: Can be rolled back if used within a transaction.
TRUNCATE: Cannot be rolled back in some databases.
Performance:
DROP: Fast, as it removes the entire table structure.
DELETE: Slower, as it deletes rows one by one and logs each deletion.
TRUNCATE: Faster than DELETE, as it deallocates data pages without logging individual row deletions.
Table Structure:
DROP: Removes the table structure and data.
DELETE: Retains the table structure.
TRUNCATE: Retains the table structure.
Triggers:
DROP: Does not fire triggers.
DELETE: Fires triggers.
TRUNCATE: Does not fire triggers.
-- DROP example
DROP TABLE Employees;
-- DELETE example
DELETE FROM Employees WHERE employee_id = 1;
-- TRUNCATE example
TRUNCATE TABLE Employees;

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

-- Step 1: Create a Database
CREATE DATABASE CompanyDB;
-- Step 2: Use the Database
USE CompanyDB;
-- Step 3: Create a Table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    salary DECIMAL(10, 2)
);

Assume that you are working on constructing a robust data model for an e-commerce company’s data warehouse. The grand nexus of this model is the "Order" fact table, interwoven with the dimensions of "Product", *Customer", and "Date". The symphony of data reveals its crescendo when you are tasked with crafting an SQL query that unites these dimensions, yielding the total revenue generated for each product on a specific date.
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
Calculate the average value of the id column for each group of rows that have the same type in the categories table.
SELECT AVG(id) FROM categories GROUP BY type

## Find the count of employees in each city?

**Answer**

```sql
SELECT city, COUNT(*) AS employee_count
FROM Employees
GROUP BY city;
```

## What is COMMIT & ROLLBACK?

**Answer**

COMMIT
Purpose: To save all changes made during the current transaction to the database.
Usage: Once you execute a COMMIT, all changes made during the transaction become permanent and visible to other users.
Syntax: COMMIT;
ROLLBACK
Purpose: To undo all changes made during the current transaction.
Usage: If an error occurs or if you decide not to save the changes, you can use ROLLBACK to revert the database to its previous state before the transaction began.
Syntax: ROLLBACK;

## Number of records after different kinds of join?

**Answer**

INNER JOIN:
Returns only the rows that have matching values in both tables.
The number of records will be equal to the number of matching rows between the two tables.
If there are no matches, the result set will be empty.
LEFT JOIN (or LEFT OUTER JOIN):
Returns all rows from the left table, and the matched rows from the right table.
If there is no match, the result is NULL on the side of the right table.
The number of records will be at least the number of rows in the left table. If there are matches, it could be more.
RIGHT JOIN (or RIGHT OUTER JOIN):
Returns all rows from the right table, and the matched rows from the left table.
If there is no match, the result is NULL on the side of the left table.
The number of records will be at least the number of rows in the right table. If there are matches, it could be more.
FULL JOIN (or FULL OUTER JOIN):
Returns all rows when there is a match in either the left or right table.
If there is no match, the result is NULL on the side that does not have a match.
The number of records will be the total number of unique rows from both tables, including matches and non-matches.
Toys and children. Given the database schema:
Children(child_name STRING, age INT)
Toys(toy_name STRING, price DECIMAL)
List(child_name STRING, toy_name STRING)
List (in alphabetical order) the names of the toys asked by children under 9 years old.
SELECT t.toy_name
FROM List l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name

WHERE c.age < 9
ORDER BY t.toy_name;

## What is the total amount spent by each child?

**Answer**

```sql
SELECT c.child_name, SUM(t.price) AS total_amount_spent
FROM List l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name
GROUP BY c.child_name;
```

## Who are the children spending over 200?

**Answer**

```sql
SELECT c.child_name, SUM(t.price) AS total_amount_spent
FROM List l
JOIN Children c ON l.child_name = c.child_name
JOIN Toys t ON l.toy_name = t.toy_name
GROUP BY c.child_name
HAVING SUM(t.price) > 200;
```

## What are Database views?

**Answer**

Database Views: Virtual tables that present data from one or more tables in a specific format or structure.
Virtual Tables: Views do not store data themselves but retrieve data from underlying tables dynamically.
Simplified Data Access: Views encapsulate complex queries and present data in a user-friendly format.
Data Abstraction: Views provide a level of abstraction, hiding the complexity of underlying table structures.
Security: Views can restrict access to specific columns or rows of data, providing controlled access to sensitive data.
Reusability: Views can be reused in multiple queries, reducing redundancy and improving maintainability.
Creating Views: Use the CREATE VIEW statement to define a view.
Querying Views: Query views like regular tables.
Updating Data Through Views: Views can be updatable under certain conditions.
Managing Views: Use ALTER VIEW to modify and DROP VIEW to remove views.
