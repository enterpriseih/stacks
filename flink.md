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
