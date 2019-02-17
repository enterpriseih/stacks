from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    # id
    'example_bash_operator',

    # True is great for atomic datasets that can easily be split into periods
    # False is great if your DAG Runs perform backfill internally.
    catchup=False,

    schedule_interval=timedelta(minutes=1),

    #
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 10, 20),
        'end_date': datetime(2018, 10, 23),
    })

t1 = BashOperator(
    task_id="echo",
    bash_command="echo 1",
    dag=dag
)
