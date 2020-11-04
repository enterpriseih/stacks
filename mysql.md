# mysql

## install

```bash
wget <http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm>
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum update
sudo yum install mysql-server
```

## start w/ docker

```
docker run -e MYSQL_ROOT_PASSWORD=123456  -p 3306:3306 -v ~/mysql:/var/lib/mysql -d mysql:5.7
```

## shutdown

```
/usr/local/mysql/bin/mysqladmin -u root -p shutdown
sudo mysqld stop
sudo /usr/local/mysql/bin/mysqld stop
brew services stop mysql

ps aux | grep mysqld
kill -TERM <PID>
```

## user

```sql
CREATE USER my_user IDENTIFIED BY 'my_password';
GRANT ALL ON * TO my_user;
```

## profile

```sql
-- show all column names
select * from information_schema.columns where TABLE_SCHEMA = 'my_table';

-- version
SHOW VARIABLES LIKE "%version%";
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

-- drop
DROP TABLE my_table
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
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
```

## mysql shell

```bash
# download
wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-8.0.18-linux-glibc2.12-x86-64bit.tar.gz

# unzip
tar -xzvf mysql-shell-8.0.18-linux-glibc2.12-x86-64bit.tar.gz

#
mv mysql-shell-8.0.18-linux-glibc2.12-x86-64bit mysql-shell
./mysql-shell/bin/mysqlsh -u <user> -h <ip>
```
