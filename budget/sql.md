Sure, here are some basic SQL syntax and commands:

1. **SELECT**: This command is used to select data from a database. The data returned is stored in a result table, called the result-set.
   ```sql
   SELECT column1, column2, ...
   FROM table_name;
   ```
   Here, `column1`, `column2`, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:
   ```sql
   SELECT * FROM table_name;
   ```

2. **UPDATE**: This command is used to modify the existing records in a table.
   ```sql
   UPDATE table_name
   SET column1 = value1, column2 = value2, ...
   WHERE condition;
   ```
   
3. **DELETE**: This command is used to delete existing records in a table.
   ```sql
   DELETE FROM table_name WHERE condition;
   ```

4. **INSERT INTO**: This command is used to insert new records in a table.
   ```sql
   INSERT INTO table_name (column1, column2, column3, ...)
   VALUES (value1, value2, value3, ...);
   ```

5. **CREATE DATABASE**: This command is used to create a new SQL database.
   ```sql
   CREATE DATABASE database_name;
   ```

6. **ALTER DATABASE**: This command is used to modify a database.
   ```sql
   ALTER DATABASE database_name
   COLLATE collation_name;
   ```

7. **CREATE TABLE**: This command is used to create a new table in a database.
   ```sql
   CREATE TABLE table_name (
   column1 datatype,
   column2 datatype,
   column3 datatype,
   ....
   );
   ```

8. **ALTER TABLE**: This command is used to add, delete/drop or modify columns in an existing table.
   ```sql
   ALTER TABLE table_name
   ADD column_name datatype;
   ```

9. **DROP TABLE**: This command is used to delete a table in a database.
   ```sql
   DROP TABLE table_name;
   ```

10. **CREATE INDEX**: This command is used to create an index (search key).
    ```sql
    CREATE INDEX index_name
    ON table_name (column1, column2, ...);
    ```

11. **DROP INDEX**: This command is used to delete an index in a table.
    ```sql
    DROP INDEX index_name;
    ```

Please note that SQL is not case sensitive: `SELECT` is the same as `select`¹. However, it's a common practice to write SQL keywords in upper-case¹.

For more detailed information, you can refer to this [SQL Syntax Guide](^1^) or this [SQL Basics Cheat Sheet](^2^).¹²

Source: Conversation with Bing, 21/12/2023
(1) SQL Syntax - W3Schools. https://www.w3schools.com/sql/sql_syntax.asp.
(2) SQL Syntax - W3Schools. https://www.w3schools.com/sql/sql_syntax.asp.
(3) SQL Basics Cheat Sheet | LearnSQL.com. https://learnsql.com/blog/sql-basics-cheat-sheet/.
(4) SQL Basics Cheat Sheet | LearnSQL.com. https://learnsql.com/blog/sql-basics-cheat-sheet/.
(5) SQL Syntax - SQL Tutorial. https://www.sqltutorial.org/sql-syntax/.
(6) SQL Commands: The Complete List (w/ Examples) – Dataquest. https://www.dataquest.io/blog/sql-commands/.
(7) SQL Quick Reference - W3Schools. https://www.w3schools.com/sql/sql_quickref.asp.