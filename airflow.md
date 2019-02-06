# airflow

## basic

```bash
# on centos
pip install cryptography
# generate frenet key for docker
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

# on mac
brew install mysql
pip install apache-airflow[all]
pip install mysqlclient
```

## cli

```bash
# create Admin
airflow create_user -r Admin -u <user_name> -e <email> -f <first_name> -l <last_name> -p <password>

# initialize database
airflow initdb

# show dags
airflow list_dags

# show tasks
airflow list_tasks tutorial
airflow list_tasks tutorial --tree

# create connection
airflow connections -a --conn_id <ftp> --conn_uri "ftp://username:password@ip:port"
airflow connections -a --conn_id <mysql> --conn_type "mysql" --conn_host "ip" --conn_login "username" --conn_password "password" --conn_port "3306"

# test job
airflow test my_dag main 20181029

# postgresql
# delete dags
delete from public.dag where dag_id = 'tutorial2';
```

## worker

```bash
# assume /data/airflow is the directory

# https://github.com/puckel/docker-airflow/blob/master/README.md#custom-airflow-plugins
# 1. edit /data/airflow/requirements.txt and mount it like
# /data/airflow/requirements.txt:/requirements.txt
# ex. add following two lines:
# pymongo
# boto3

# 2. add an airflow worker docker instance
# hostname is the ip address of host machine so that the remote log is accessible
# docker command is worker -q

# 3. clone my dag files
cd /data/airflow/dags
git clone airflow_dag_project

# 4. add plugins
cd /data/airflow/plugins
git clone https://github.com/airflow-plugins/mongo_plugin

# 5. edit permission of airflow/logs
cd /data/airflow
chmod -R 757 logs
```
