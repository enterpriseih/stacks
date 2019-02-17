from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from airflow.contrib.hooks.ftp_hook import FTPHook

import io
import csv
from datetime import datetime, timedelta
import pendulum
local_tz = pendulum.timezone('Asia/Shanghai')
now = datetime.now(local_tz)

dag = DAG(
    'example_ftp_csv_mysql',
    catchup=False,
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 11, 9, tzinfo=local_tz),
        'email': ['airflow@example.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 0,
        'retry_delay': timedelta(minutes=1),
    }
)

HEADERS = ['field1', 'field2']
AUX_FIELDS = ['field3', 'field4']


def main():
    ftp = FTPHook(ftp_conn_id='my_ftp')
    ftp.get_conn().encoding = 'utf-8'

    files = ftp.list_directory('/my_dir/')
    for file in files:
        result = []
        remote_path = '/my_dir/' + file
        buffer = io.BytesIO()

        # downloading might take time
        ftp.retrieve_file(remote_path, buffer)
        buffer.seek(0)
        reader = csv.DictReader(
            io.TextIOWrapper(buffer, newline=None), delimiter=',')

        for i, row in enumerate(reader):
            # header
            if i == 0:
                continue

            # data
            r = [row[field] if row[field] != '' else None for field in HEADERS]

            # append
            r = r + [now, 'airflow', now, 'airflow', remote_path]
            result.append(r)

    # dump
    target = MySqlHook(mysql_conn_id='my_mysql')
    target.insert_rows(
        table='my_table',
        rows=result,
        commit_every=5000,
        target_fields=HEADERS+AUX_FIELDS
    )
    return


t1 = PythonOperator(
    task_id='main',
    python_callable=main,
    dag=dag
)
