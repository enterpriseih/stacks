# mongodb

## basic
```bash
# install on centos
sudo vi /etc/yum.repos.d/mongodb-org-3.4.repo
# add
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=<https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.4/x86_64/>
gpgcheck=1
enabled=1
gpgkey=<https://www.mongodb.org/static/pgp/server-3.4.asc>

sudo yum install -y mongodb-org

# dump
./mongodump --host <host> --port <port> --username <username> --password <password> --out <output_dir> --db <db>

# restore
mongorestore --host <host> --port <port> --username <username> --password <password> <backup_dir>

# start service
sudo service mongod start
```

## shell
```js
```
