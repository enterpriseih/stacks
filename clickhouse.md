# clickhouse

## install

```bash
# https://clickhouse.tech/docs/en/getting-started/install/

# add repo
sudo yum install yum-utils
sudo rpm --import https://repo.clickhouse.tech/CLICKHOUSE-KEY.GPG
sudo yum-config-manager --add-repo https://repo.clickhouse.tech/rpm/stable/x86_64

# install
sudo yum install clickhouse-server clickhouse-client

```

## config

```bash
# edit paths to config.xml
# change data path with /var/lib/clickhouse/ to /data/clickhouse/
# change log path /var/log/clickhouse-server/ to /data/log/clickhouse/
vim /etc/clickhouse-server/config.xml

# update permission
chown clickhouse:clickhouse /data/clickhouse/
chown clickhouse:clickhouse /data/log/clickhouse/
```

## start/stop

```bash
# service will be started with clickhouse:clickhouse
# see /etc/systemd/system/clickhouse-server.service

# start server single node
systemctl start clickhouse-server

# stop
systemctl stop clickhouse-server

# reload config
sudo systemctl reload clickhouse-server

# check status
systemctl status clickhouse-server

# check full systemctl log
journalctl -u clickhouse-server
systemctl -l status clickhouse-server
```

## start client

```bash
# client from local
clickhouse-client

# multiple line client
clickhouse-client -m
```

## http

```bash
curl 'http://<ip>:8123'
```

## sql

#### database

```sql
CREATE DATABASE IF NOT EXISTS tutorial

-- show db
SHOW DATABASES;
```

#### table

```bash
#insert from csv
clickhouse-client --query "INSERT INTO tutorial.hits_v1 FORMAT TSV" --max_insert_block_size=100000 < hits_v1.tsv

```

```sql
SELECT COUNT(*) FROM tutorial.hits_v1;

-- show table
SHOW TABLES from <db>;
```

#### partition

```sql
-- show partition
SELECT partition, name, active　FROM system.parts　WHERE table = 'visits_v1';
-- or go to <data_dir>/<database>/<table>
```

## operation

#### connection

```sql
-- check connections
SELECT * FROM system.metrics WHERE metric LIKE '%Connection';
```

#### storage

```sql
-- show storage
SELECT name,path,formatReadableSize(free_space) AS free,formatReadableSize(total_space) AS total,formatReadableSize(keep_free_space) AS reserved FROM system.disks;

-- show db storage
SELECT database, formatReadableSize(sum(bytes_on_disk)) on_disk FROM system.parts GROUP BY database;

-- show column storage
SELECT database, table, column, any(type), sum(column_data_compressed_bytes) AS compressed, formatReadableSize(sum(column_data_uncompressed_bytes)AS uncompressed, round(uncompressed / compressed, 2) AS ratio, compressed / sum(rows) AS bpr, sum(rows) FROM system.parts_columns WHERE active AND database != 'system' GROUP BY database, table, column ORDER BY database ASC, table ASC, column ASC;
```

#### query

```sql
-- show slow queries
SELECT user, client_hostname,client_name,formatDateTime(query_start_time, '%T') AS started, query_duration_ms / 1000 AS sec, round(memory_usage / 1048576) AS MEM_MB, result_rows AS RES_CNT, result_bytes / 1048576 AS RES_MB, read_rows AS R_CNT, round(read_bytes / 1048576) AS R_MB, written_rows AS W_CNT, round(written_bytes / 1048576) AS W_MB, query FROM system.query_log WHERE type = 2 ORDER BY query_duration_ms DESC LIMIT 10;

-- show current queries
SELECT query_id, user, address, query  FROM system.processes ORDER BY query_id;
show processlist；

-- kill query
KILL QUERY WHERE query_id = <query_id>;
```

#### mutation

```sql
-- show current mutation
SELECT database, table, mutation_id, command, create_time, is_done FROM system.mutations;

-- kill mutation
KILL MUTATION WHERE mutation_id = <mutation_id>;
```
