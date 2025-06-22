# 通过创建马里奥游戏角色数据库学习关系型数据库 PostgreSQL

## 简介

关系型数据库通过关系将数据组织到表格 `table` 中。

## 笔记

PostgreSQL > 数据库 (database) > 表 (table) > 列和行(COLUMN/ROW)

> [!NOTE]
> PostgreSQL 和 Excal 很类似：
>
> - PostgreSQL相当于Excel
> - database相当于Excal文件（工作簿）
> - table相当于某个Excel文件的工作表
> - COLUMN和ROW相当于工作表的表头标题和行

### 一、打开 psql 命令行

在 Bash 中输入：

```sql
psql --username=freecodecamp --dbname=postgres
```

### 二、列出 (list) 所有数据库 (database)

```sql
\l
```

就算没有创建数据库，使用此命令也会列出(list)好几个数据库，因为这些是默认存在的数据库。

### 三、数据库操作 

> [!NOTE]
> 所有包含大写字母的命令都需要有结束符 `;`，命令行提示符是 `=>`，命令没有结束时，提示符是 `->`，以下所有命令 `<>`中的内容为需要替换的内容，`[]`中的内容为可选的。

#### 3.1 创建数据库 `CREATE DATABASE`

```sql
CREATE DATABASE <database_name>;
```

#### 3.2 删除数据库 `DROP DATABASE`

```sql
DROP DATABASE <database_name>;
```

#### 3.3 连接数据库

```sql
\c <database_name>
```

在某个数据库(database)中创建表(table)之前，需要先连接(connect)数据库。

#### 3.4 重命名数据库 `ALTER DATABASE`

```sql
ALTER DATABASE <database_name> RENAME TO <new_database_name>;
```

#### 3.4 展示(display)数据库(database)中所有表(table)

```sql
\d
```

### 四、表(table)操作

#### 4.1 创建表 `CREATE TABLE`

数据库(database)中默认没有表(table)，需要自己在连接到的数据库中创建表。

```sql
CREATE TABLE <table_name>();
```

> [!NOTE]
> 不要忘记括号

也可以创建表时，顺便创建列(column)：

```sql
CREATE TABLE <table_name(column_name DATATYPE[ CONSTRAINTS])>;
```

#### 4.2 展示(display)表(table)的详细信息

```sql
\d table_name
```

#### 4.3 删除表 `DROP TABLE`

```sql
DROP TABLE <table_name>;
```

### 五、表(table)中的列(column)操作

#### 5.1 添加列 `ADD COLUMN`

表(table)中默认没有列(column)，需要自行创建。

```sql
ALTER TABLE <table_name> ADD COLUMN <column_name> <DATATYPE> [<CONSTRAINT>];
```

创建列时，需要设置此列数据的数据类型 DATATYPE，常见数据类型如下：

- `INT` 整数
- `VARCHAR(n)`字符串，n表示字符串的最大长度，如 `VARCHAR(30)` 表示字符串最大长度为30个字符
- `NUMERIC(m, n)`小数，最多有m个有效位数（小数位数+整数位数），小数位数为n位。例如`NUMERIC(4, 1)`表示最多有4位有效数字，1位小数，如999.9
- `SERIAL` 序列，从1开始按照添加列的顺序自动添加序号，DATATYPE CONSTRAINT相当于 `INT NOT NULL`

常见限制条件CONSTRAINT：

- `NOT NULL` 非空，禁止插入空行

#### 5.2 重命名列 `RENAME COLUMN`

```sql
ALTER TABLE <table_name> RENAME COLUMN <column_name> TO <new_name>;
```

#### 5.3 为已有列添加限制条件

```sql
ALTER TABLE <table_name> ALTER COLUMN <column_name> SET <CONSTRAINT>;
```

例如：

```sql
ALTER TABLE <table_name> ALTER COLUMN <column_name> SET NOT NULL;
```

### 六、表(table)中行(row)操作 

#### 6.1 插入行 `INSERT INTO`

```sql
INSERT INTO <table_name(column_1, column_2, ...)> VALUES(<value1, value2, ...>);
```

column_1, column_2, ... 表示除了数据类型(DATATYPE)是 `SERIAL`的列之外的所有列。value1, value2, ...表示除数据类型(DATATYPE)是 `SERIAL`的列之外的所有列对应的值。数据类型是`VARCHAR`的插入行时需要使用单引号`'`包裹

批量插入多行，`VALUES`每行使用`()`包裹，`,`分隔，例如：

```sql
INSERT INTO characters(name, homeland, favorite_color)
VALUES('Mario', 'Mushroom Kingdom', 'Red'),
('Luigi', 'Mushroom Kingdom', 'Green'),
('Peach', 'Mushroom Kingdom', 'Pink');
```

#### 6.2 删除行 `DELETE FROM`

```sql
DELETE FROM <table_name> WHERE <condition>;
```

根据条件(condition)删除行，例如`username='Luigi'`，删除列名为username，值为'Luigi'的单元格所在的行。

#### 6.3 更新某单元格的值 `UPDATE`

```sql
UPDATE <table_name> SET <column_name=new_value> WHERE <condition>;
```

与6.2 删除行条件(condition)的写法类似。

### 七、查表和筛选排序 `SELECT`

#### 7.1 查询列名信息

查询列名、数据类型、限制条件等信息：

```sql
SELECT <columns> FROM <table_name>;
```

查询所有：

```sql
SELECT * FROM <table_name>;
```

查询某几列：

```sql
SELECT <column1, column2, ...> FROM <table_name>;
```

#### 7.2 条件查询

```sql
SELECT <columns> FROM <table_name> WHERE <condition>;
```

与6.2 删除行条件(condition)的写法类似。

#### 7.3 排序

```sql
SELECT <columns> FROM <table_name> ORDER BY <column_name>;
```

根据某列进行排序，一般column_name为数据类型是`SERIAL`的列，常用命令：

```sql
SELECT * FROM <table_name> ORDER BY <column_name>;
```

### 八、键(key)

#### 8.1 添加主键 `ADD PRIMARY KEY`

```sql
ALTER TABLE <table_name> ADD PRIMARY KEY(<column_name>);
```

将某列设置为主键(primary key)，此列对应的单元格可以唯一确定某一行。每个表(table)有且只有一个主键。

#### 8.2 删除主键 `DROP CONSTRAINT`

```sql
ALTER TABLE <table_name> DROP CONSTRAINT <constraint_name>;
```

constraint_name一般为 `<column_name>_pkey`，即 `列名_pkey`

#### 8.3 创建外键 `REFERENCES`

```sql
ALTER TABLE <table_name> ADD COLUMN <column_name> <DATATYPE> REFERENCES <referenced_table_name(referenced_column_name)>;
```

创建一个表示外键的列，referenced_table_name(referenced_column_name)一般是 `主键所在的表(主键的列名)`，通过外键和主键形成关系。

#### 8.4 强制外键和主键一一对应（一对一关系）

```sql
ALTER TABLE <table_name> ADD UNIQUE(<column_name>);
```

column_name为外键所在的列名。

#### 8.5 主键与外键形成一对多关系

```sql
ALTER TABLE <table_name> ADD COLUMN <column_name> <DATATYPE> <CONSTRAINT> REFERENCES <referenced_table_name(referenced_column_name)>;
```

#### 8.6 将已有的列(column)设置为外键

```sql
ALTER TABLE <table_name> ADD FOREIGN KEY(<column_name>) REFERENCES <referenced_table(referenced_column)>;
```

#### 8.7 复合主键(composite primary key)

前面设置的主键 只是将一列(column)设置为主键，还可以将多列设置为主键（复合主键）：

```sql
ALTER TABLE <table_name> ADD PRIMARY KEY(<column1, column2, ...>);
```

将 column1, column2, ... 设置为主键

> [!NOTE]
> 每个表有且只有一个主键，复合主键算是一个主键。

### 九、通过主键(primary key)和外键(foreign key)整合(join)数据

#### 9.1 整合(join)两个表(table)

```sql
SELECT <columns> FROM <table_1> FULL JOIN <table_2> ON <table_1>.primary_key_column = <table_2>.foreign_key_column;
```

columns常用 `*` 表示

#### 9.2 整合(join)多个表(table)

```sql
SELECT <columns> FROM <junction_table>
FULL JOIN <table_1> ON <junction_table>.foreign_key_column = <table_1>.primary_key_column
FULL JOIN <table_2> ON <junction_table>.foreign_key_column = <table_2>.primary_key_column;
```