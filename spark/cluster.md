# spark cluster

## install
```bash
# download
wget http://mirror.bit.edu.cn/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz

# unzip
tar xf spark-2.4.0-bin-hadoop2.7.tgz
cd spark-2.4.0-bin-hadoop2.7

# start master
./sbin/start-master.sh

# start slave
./sbin/start-slave.sh spark://my_ip:7077
```
