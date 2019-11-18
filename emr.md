# emr

## system

```bash
# timezone
cat /etc/sysconfig/clock
ls /usr/share/zoneinfo
```

## aws

```bash
# show all cluster
aws emr list-clusters --active

# describe cluster
aws emr describe-cluster --cluster-id <id>
```

## error

### libm.so.6 link broken

```bash
# when run hadoop version
# Error: failed /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-0.43.amzn1.x86_64/jre/lib/amd64/server/libjvm.so, because libm.so.6: symbol __strtof128_nan, version GLIBC_PRIVATE not defined in file libc.so.6 with link time reference

# find link broken
ll /lib64/libm.so.6

# fix link
ldconfig
```
