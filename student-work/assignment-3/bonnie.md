# Bonnie (TzuChen) Lin
My favorite programming language is sql because compared to other programming languages such as C or Rust, it is relatively easy to understand and learn. 
## Example Code
``` 
SELECT first_name, last_name, salary 
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC;
```
### Code Explanation
The above code selects three columns `first_name`, `last_name` and `salary` from the table `employees`. With the filter where the employees belong to the `IT` department. The last line specify the order of output wanting the employees to be sorted by descending salary. To run it, you need a database (such as SQLite, MySQL, or PostgreSQL) that contains an `employees` table with these columns.


