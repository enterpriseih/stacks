# zookeeper

## mac

```bash
# install on mac
brew install zookeeper

# connect to a zk
zkCli -server <ip>
```

## install

0.  export ZOOKEEPER_HOME=/usr/lib/zookeeper/

1.  download zookeeper at /usr/lib/zookeeper/

2.  setup conf/zoo.cfg

```cfg
maxClientCnxns=0
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/var/lib/zookeeper
clientPort=2181
autopurge.purgeInterval=24

server.0=<ip>:2888:3888
server.1=<ip>:2888:3888
```

3.  create myid at dataDir

```bash
cd /var/lib/zookeeper
touch myid
cat 1 > myid
```

4.  start server

```bash
/usr/lib/zookeeper/bin/zkServer.sh start
```

5.  see status

```bash
/usr/lib/zookeeper/bin/zkCli.sh -server 127.0.0.1:2181
```

6.  check connection

```bash
/usr/lib/zookeeper/bin/zkCli.sh -server 127.0.0.1:2181
```
