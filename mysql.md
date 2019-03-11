# mysql

## install

```bash
wget <http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm>
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum update
sudo yum install mysql-server
```

## user

```sql
CREATE USER my_user IDENTIFIED BY 'my_password';
GRANT ALL ON * TO my_user;
```

## database & table

```sql
-- create db
CREATE DATABASE my_db;

-- use db
use my_db

-- list tables
show tables;

-- create tables
CREATE TABLE my_table( my_field VARCHAR(32));

-- show create sql
SHOW CREATE TABLE my_table;

-- rename table
ALTER TABLE my_table rename to new_table;

-- change column type or name
ALTER TABLE my_table change my_column my_column varchar(20);
ALTER TABLE my_table modify my_column BIGINT NOT NULL;

-- delete column
ALTER TABLE my_table drop column my_column

-- add primary key
ALTER TABLE my_table add primary key(my_key);

-- delete primary key
ALTER TABLE my_table drop primary key;

-- auto_increment
ALTER TABLE my_table AUTO_INCREMENT = 1010;
```

## query

```sql
-- describe
describe my_table;

-- select
select * from my_table;

-- delete
delete from my_table where my_column > 0;

-- insert
insert into my_table (my_column1, my_column2, my_column3) values ('my_value1', 'my_value2', 'my_value3');
```

## process

```sql
-- show process
SHOW FULL PROCESSLIST
```
