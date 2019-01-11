# Start a HTTPS Server

## install

```bash
# add repo
touch /etc/yum.repos.d/nginx.repo

# open nginx.repo and add
[nginx]
name=nginx repo
baseurl=<http://nginx.org/packages/centos/6/$basearch/>
gpgcheck=0
enabled=1
# install on centos
yum install nginx
```

## certificate

```bash
# create certificate
mkdir /etc/nginx/ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
# when asking infos such as Country Name, type
```

## server

```bash
# configure nginx

vim /etc/nginx/nginx.conf

# in file add

http{
    server {
        listen 80 default*server;
        listen [::]:80 default_server ipv6only=on;
        listen 433 ssl;
        root /data/project/dist;
        index index.html;
        server_name \_;
        ssl_certificate "/etc/nginx/ssl/nginx.crt";
        ssl_certificate_key "/etc/nginx/ssl/nginx.key";
        location / {
            try_files $uri $uri/ =404;
        }
    }
}

# start service

systemctl start nginx

# restart service

service nginx restart

```

## check

```bash
# check syntax

nginx -t -c /etc/nginx/nginx.conf

```
