from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

dag = DAG(
    'example_email_operator',
    catchup=False,
    schedule_interval="@hourly",
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 10, 20),
        'end_date': datetime(2018, 10, 23),

        'email': ['airflow@example.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': timedelta(seconds=10),
    })

t1 = EmailOperator(
    task_id="simple_email_opearetor",
    to=["receiver@example.com"],
    subject="Testing Email Operator",
    html_content="<h3>Welcome to Airflow</h3>",
    dag=dag,
)
