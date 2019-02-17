from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime

dag = DAG(
    'example_mysql_operator_multiple',
    catchup=False,
    schedule_interval="@hourly",
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 10, 20),
        'end_date': datetime(2018, 10, 23),
    })

t1 = MySqlOperator(
    task_id="mysql",
    mysql_conn_id="mysql_conn_1",
    sql=[
        "USE my_database",
        "INSERT INTO my_database.my_table (id) VALUES ('2')"
    ],
    dag=dag
)
