from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime, timedelta
import pendulum
local_tz = pendulum.timezone('Asia/Shanghai')
now = datetime.now(local_tz)

dag = DAG(
    'example_mysql_operator',
    catchup=False,
    schedule_interval="@hourly",
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 10, 23, tzinfo=local_tz),
        'email': ['airflow@example.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }
)


def main():
    # fetch source data
    source = MySqlHook(mysql_conn_id="my_mysql")
    sql1 = """
        select field1,field2
        from my_db.my_table
        where field1<>''
        group by field2
    """
    result = source.get_records(sql1)

    # apply transformation
    result = [list(r)+[now, "airflow"] for r in result]

    # dump
    target = MySqlHook(mysql_conn_id="my_mysql2")
    target.insert_rows(
        table="my_db2.my_table2",
        rows=result,
        target_fields=['field1', 'field2', 'field3', 'field4'])

    # delete
    target.run(
        'DELETE FROM my_db2.my_table2 where field3 < "{0}"'
        .format(now.strftime("%Y-%m-%d %H:%M:%S")))
    return


t1 = PythonOperator(
    task_id="main",
    python_callable=main,
    dag=dag
)
