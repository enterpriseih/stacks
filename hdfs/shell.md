# FS Shell

## basic

```bash
# install on mac
brew search hadoop

# check version
hadoop version

# checksum
hadoop fs -checksum <URI>

# show free space
hadoop fs -df <path>

# count
hadoop fs -count <path>>
```

## file & pathectory

```bash
# list files
hadoop fs -ls <URI>

# put file
hadoop fs -put <localsrc> <dst>

# rm file/pathector
hadoop fs -rm <URI>
hadoop fs -rm -r <path>

# create dir
hadoop fs -mkpath -p <path>

# find file name that match a pattern
hadoop fs -find <path> -name <pattern> -print
```

## snapshot

```bash
# Admin ops require superuser privilege
# allow
hdfs dfsadmin -allowSnapshot <path>

# disallow
hdfs dfsadmin -disallowSnapshot hdfs://10.132.144.39:8020/temp/

# User ops
# create
hdfs dfs -createSnapshot <path> [<snapshotName>]

# delete
hdfs dfs -deleteSnapshot <path> [<snapshotName>]
```