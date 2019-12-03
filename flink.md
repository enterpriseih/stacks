# flink

## basic

```bash
# 配置 username 和 password 验证
yum install httpd-tools

# create file
htpasswd -c /etc/flink/.htpasswd flink

# add more account
htpasswd /etc/flink/.htpasswd flink2
```

## job

```bash
# run job
flink run -c <main_class> <path_to_jar>
```

## docker

### docker-compose.yml

```yml
version: "2"
services:
  jobmanager:
    image: flink:latest
    environment:
      JOB_MANAGER_RPC_ADDRESS: jobmanager
    stdin_open: true
    tty: true
    ports:
      - 8081:8081/tcp
      - 6123:6123/tcp
    command:
      - jobmanager
    labels:
      io.rancher.container.pull_image: always
      io.rancher.scheduler.affinity:host_label: flink=true
  taskmanager:
    image: flink:latest
    environment:
      JOB_MANAGER_RPC_ADDRESS: jobmanager
    stdin_open: true
    tty: true
    links:
      - jobmanager:jobmanager
    ports:
      - 6121:6121/tcp
      - 6122:6122/tcp
    command:
      - taskmanager
    labels:
      io.rancher.container.pull_image: always
      io.rancher.scheduler.affinity:host_label: flink=true
```

### rancher-compose.yml

```yml
version: "2"
services:
  jobmanager:
    scale: 1
    start_on_create: true
  taskmanager:
    scale: 1
    start_on_create: true
```
