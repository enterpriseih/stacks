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

## /etc/nginx/nginx.conf

```bash
# http
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

# https server only
server {
    listen       3001 ssl;
    root         /data/project/dist;
    index index.html;
    server_name  my.ip;
    ssl_certificate "/etc/nginx/ssl/nginx.crt";
    ssl_certificate_key "/etc/nginx/ssl/nginx.key";
}

# https

server {
    listen       443;
    server_name  <my_domain>;

    proxy_read_timeout 300s;

    gzip on;
    gzip_min_length 256;
    gzip_comp_level 3;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_vary on;
    gzip_proxied any;
    #禁用 IE 6 gzip
    gzip_disable msie6;
    gzip_types text/plain application/javascript application/x-javascript text/javascript text/css application/xml application/font-woff application/otf application/font-woff2;

    location ^~ / {
            root <path/to/index/html/dir>;
            try_files $uri $uri/ /index.html;
    }

    location /api/ {
        proxy_pass   http://127.0.0.1:<port>/api/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }

    location ~* \.(js|css)$ {
        expires 1d;
        access_log off;
    }

    location ~* \.(otf|swoff|swoff2)$ {
        expires 30d;
        access_log off;
    }
}

# start service
systemctl start nginx

# restart service
service nginx restart

# check status
service nginx status -l
```

## check

```bash
# check syntax

nginx -t -c /etc/nginx/nginx.conf
```

## docker

/path/to/index/html/folder:/usr/share/nginx/html:ro
