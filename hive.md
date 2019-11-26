# hive

()[https://docs.cloudera.com/documentation/enterprise/5-6-x/topics/cdh_ig_hive_installation.html]

## basic

data stored in hdfs /user/hive/warehouse

use remote mode, start metastore(aka HCatalog) before hiveserver2

add s3a key in core-site.xml and create external table in hive

## permission

by default everyone is superadmin

## metastore

```bash
# start metastore
sudo service hive-metastore start

# Test connectivity to metastore
hive –e “show tables;”
```

## hiveserver2

```bash
# start hiveserver2
sudo service hive-server2 start

# stop hiveserver2
sudo service hive-server2 stop

# verify using beeline
```

## beeline

```bash
# start cli
/usr/lib/hive/bin/beeline

# connect to db
!connect jdbc:hive2://localhost:10000 <javax.jdo.option.ConnectionUserName> <javax.jdo.option.ConnectionPassword>  org.apache.hive.jdbc.HiveDriver

# verify hiveserver2 is running
show tables;
```

## shell

```bash
# enter shell
hive
```

## hive sql

```sql
DROP DATABASE IF EXISTS my_db;
```

## hive-site.xml

```xml
<property>
  <name>hive.execution.engine</name>
  <value>tez</value>
</property>

<!-- dir -->
<property>
  <name>hive.exec.scratchdir</name>
  <value>/user/hive/tmp</value>
</property>
<property>
  <name>hive.metastore.warehouse.dir</name>
  <value>/user/hive/warehouse</value>
</property>
<property>
  <name>hive.querylog.location</name>
  <value>/user/hive/log</value>
</property>

<!-- fs -->
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://ip:8020</value>
</property>

<!-- metastore -->
<property>
  <name>hive.metastore.uris</name>
  <value>thrift://ip:9083</value>
  <description>JDBC connect string for a JDBC metastore</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:mysql://<ip>:3306/<table>?createDatabaseIfNotExist=true</value>
  <description></description>
</property>

<property>
  <name>javax.jdo.option.ConnectionDriverName</name>
  <value>org.mariadb.jdbc.Driver</value>
  <description></description>
</property>

<property>
  <name>javax.jdo.option.ConnectionUserName</name>
  <value>hive</value>
  <description>username to use against metastore database</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionPassword</name>
  <value></value>
  <description>password to use against metastore database</description>
</property>

<!-- hiveserver2 -->
<property>
   <name>hive.server2.allow.user.substitution</name>
   <value>true</value>
</property>

<property>
   <name>hive.server2.enable.doAs</name>
   <value>true</value>
</property>

<property>
   <name>hive.server2.thrift.port</name>
   <value>10000</value>
</property>

<property>
   <name>hive.server2.thrift.http.port</name>
   <value>10001</value>
</property>
```
