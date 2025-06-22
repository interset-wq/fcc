# Learn Relational Databases by Building a Database of Video Game Characters

## Abatract

A relational database organizes data into tables that are linked together through relationships.

In this 165-lesson course, you will learn the basics of a relational database by creating a PostgreSQL database filled with video game characters.

## Note

PostgreSQL > database > table > cols and rows

### open psql command line

You will use the Psql terminal application to interact with it. Log in by typing `psql --username=freecodecamp --dbname=postgres` into the terminal and pressing enter.

### list all database

First thing to do is see what databases are here. Type `\l` into the prompt to list them.

### CREATE DATABASE

The databases you see are there by default. You can make your own like this:

    CREATE DATABASE database_name;

The capitalized words are keywords telling PostgreSQL what to do. The name of the database is the lowercase word. Note that all commands need a semi-colon (`;`) at the end. 

### drop DATABASE

    DROP DATABASE database_name;

### connect database

You can connect to a database by entering `\c database_name`. You need to connect to add information. 

### display tables in database

A database is made of tables that hold your data. Enter `\d` to display the tables.

### create table

Looks like there's no tables or relations yet. Similar to how you created a database, you can create a table like this:

    CREATE TABLE table_name();

Note that the parenthesis are needed for this one. It will create the table in the database you are connected to. 

### display detailed info of table

ou can view more details about a table by adding the table name after the display command like this: `\d table_name`

### add col

Tables need columns to describe the data in them, yours doesn't have any yet. Here's an example of how to add one:

    ALTER TABLE table_name ADD COLUMN column_name DATATYPE;

Add a column to second_table named first_column. Give it a data type of INT. `INT` stands for integer. Don't forget the semi-colon.

A common data type is `VARCHAR`. It's a short string of characters. You need to give it a maximum length when using it like this: `VARCHAR(30)` The 30 means the data in it can be a max of 30 characters. 

Give it a type of `NUMERIC(4, 1)`. That data type is for decimals. `NUMERIC(4, 1)` has up to four digits and one of them has to be to the right of the decimal.

The `SERIAL` type will make your column an INT with a NOT NULL constraint, and automatically increment the integer when a new row is added.  Add a constraint by putting it right after the data type. Here's an example: 

    ALTER TABLE table_name ADD COLUMN column_name DATATYPE CONSTRAINT;

EXAMPLE:

    ALTER TABLE table_name ADD COLUMN column_name DATATYPE NOT NULL;

### remove col

Those are some good looking columns. You will probably need to know how to remove them. Here's an example:

    ALTER TABLE table_name DROP COLUMN column_name;

### rename col

Here's how you can rename a column:

    ALTER TABLE table_name RENAME COLUMN column_name TO new_name;

---

> [!NOTE]
> Like Excal worksheet, a database also has many tables.
> 
> Like Excel worksheet, we need cols and rows. Above is adding cols. Below is adding rows with the rol name that added before.

### insert row

Rows are the actual data in the table. You can add one like this:

    INSERT INTO table_name(column_1, column_2) VALUES(value1, value2);

The username column expects a VARCHAR, so you need to put Samus in single quotes like this: 'Samus'. The first parenthesis is for the column names, you can put as many columns as you want. The second parenthesis is for the values for those columns. 

### insert rows

Adding rows one at a time is quite tedious. Here's an example of how you could have added the previous three rows at once:

    INSERT INTO characters(name, homeland, favorite_color)
    VALUES('Mario', 'Mushroom Kingdom', 'Red'),
    ('Luigi', 'Mushroom Kingdom', 'Green'),
    ('Peach', 'Mushroom Kingdom', 'Pink');

### query table

You can view the data in a table by querying it with the SELECT statement. Here's how it looks:

    SELECT columns FROM table_name;

We often use:

    SELECT * FROM table_name;

Use a SELECT statement to view all the columns in second_table. Use an asterisk (*) to denote that you want to see all the columns.

### delete row

Here's an example of how to delete a row:

    DELETE FROM table_name WHERE condition;

Remove Luigi from your table. The condition you want to use is `username='Luigi'`.

### drop table

Drop table from your database. Here's an example:

    DROP TABLE table_name;

### rename database

You can rename a database like this:

    ALTER DATABASE database_name RENAME TO new_database_name;

### update value

You can change a value like this:

    UPDATE table_name SET column_name=new_value WHERE condition;

### in order

Actually, you should put that in order. Here's an example:

    SELECT columns FROM table_name ORDER BY column_name;

We always use:

    SELECT * FROM table_name ORDER BY column_name;

View all the data again, but put it in order by character_id.

### primary key

It looks good. Next, you are going to add a primary key. It's a column that uniquely identifies each row in the table. Here's an example of how to set a PRIMARY KEY:

    ALTER TABLE table_name ADD PRIMARY KEY(column_name);

The name column is pretty unique, why don't you set that as the primary key for this table.

You should set a primary key on every table and there can only be one per table. 

### drop primary key

Here's an example of how to drop a constraint:

    ALTER TABLE table_name DROP CONSTRAINT constraint_name;

Drop the primary key on the name column. You can see the constraint name is characters_pkey.

### foreign key

To know what row is for a character, you need to set a foreign key so you can relate rows from this table to rows from your characters table. Here's an example that creates a column as a foreign key:

    ALTER TABLE table_name ADD COLUMN column_name DATATYPE REFERENCES referenced_table_name(referenced_column_name);

That's quite the command. In the more_info table, create a character_id column. Make it an INT and a foreign key that references the character_id column from the characters table. Good luck.

### UNIQUE

here's your foreign key at the bottom. These tables have a "one-to-one" relationship. One row in the characters table will be related to exactly one row in more_info and vice versa. Enforce that by adding the `UNIQUE` constraint to your foreign key. Here's an example:

    ALTER TABLE table_name ADD UNIQUE(column_name);

### NOT NULL

The column should also be NOT NULL since you don't want to have a row that is for nobody. Here's an example:

    ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;

Add the NOT NULL constraint to your foreign key column.

### view via condition

Instead of viewing all the rows to find his id, you can just view his row with a WHERE condition. You used several earlier to delete and update rows. You can use it to view rows as well. Here's an example:

    SELECT columns FROM table_name WHERE condition;

A condition you used before was username='Samus'. Find Toad's id by viewing the character_id and name columns from characters for only his row.

---

### Create table with col

Next, you will make a sounds table that holds filenames of sounds the characters make. You created your other tables similar to this:

    CREATE TABLE table_name();

Inside those parenthesis you can put columns for a table so you don't need to add them with a separate command, like this:

    CREATE TABLE table_name(column_name DATATYPE CONSTRAINTS);

Create a new table named sounds. Give it a column named sound_id of type SERIAL and a constraint of PRIMARY KEY.

### one-to-many

You want to use character_id as a foreign key again. This will be a "one-to-many" relationship because one character will have many sounds, but no sound will have more than one character. Here's the example again:

    ALTER TABLE table_name ADD COLUMN column_name DATATYPE CONSTRAINT REFERENCES referenced_table_name(referenced_column_name);

Add a column to sounds named character_id. Give it the properties INT, NOT NULL, and set it as a foreign key that references character_id from characters.

### set an existing col as foreign key

The foreign keys you set before were added when you created the column. You can set an existing column as a foreign key like this:

    ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES referenced_table(referenced_column);

Set the character_id column you just added as a foreign key that references the character_id from the characters table.

### composite primary key

Every table should have a primary key. Your previous tables had a single column as a primary key. This one will be different. You can create a primary key from two columns, known as a composite primary key. Here's an example:

    ALTER TABLE table_name ADD PRIMARY KEY(column1, column2);

Use character_id and action_id to create a composite primary key for this table.

### JOIN two tables

You can see the character_id there so you just need to find the matching id in the characters table to find out who it's for. Or... You added that as a foreign key, that means you can get all the data from both tables with a JOIN command:

    SELECT columns FROM table_1 FULL JOIN table_2 ON table_1.primary_key_column = table_2.foreign_key_column;

###

Enter a join command to see all the info from both tables. The two tables are characters and more_info. The columns are the character_id column from both tables since those are the linked keys.

This shows the "one-to-many" relationship. You can see that some of the characters have more than one row because they have many sounds. How can you see all the info from the characters, actions, and character_actions tables? Here's an example that joins three tables:

    SELECT columns FROM junction_table
    FULL JOIN table_1 ON junction_table.foreign_key_column = table_1.primary_key_column
    FULL JOIN table_2 ON junction_table.foreign_key_column = table_2.primary_key_column;

Congratulations on making it this far. This is the last step. View all the data from characters, actions, and character_actions by joining all three tables. When you see the data, be sure to check the "many-to_many" relationship. Many characters will have many actions.