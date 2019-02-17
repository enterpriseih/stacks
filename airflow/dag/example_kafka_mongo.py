from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from confluent_kafka import Producer
from pymongo import MongoClient

from datetime import datetime, timedelta
import json
import pendulum

# time
LOCAL_TZ = pendulum.timezone('Asia/Shanghai')
NOW = datetime.now(LOCAL_TZ)

# kafka
KAFKA_TOPIC = 'my_topic'
KAFKA_CONFIG = {
    'bootstrap.servers': '<ip1>:9092,<ip2>:9092,<ip3>:9092',
    'group.id': 'airflow',
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
    # auth
    'sasl.username': 'my_username',
    'sasl.password': 'my_password',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'PLAIN',
}
producer = Producer(KAFKA_CONFIG)

# mongodb
CLIENT = MongoClient('<ip>',
                     # auth
                     username='my_username2',
                     password='my_password2',
                     authSource='my_source',
                     authMechanism='SCRAM-SHA-1')
db = CLIENT['my_collection']

#  dag
dag = DAG(
    'example_kafka_mongo',
    catchup=False,
    schedule_interval="*/5 * * * *",
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 12, 7, tzinfo=LOCAL_TZ),
        'email': ['airflow@example.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }
)


def delivery_callback(err, msg):
    if err is not None:
        print('Message delivery failed: {0}'.format(err))
    else:
        print('Message delivered to {0} [{1}]'.format(
            msg.topic(), msg.partition()))


def main():
    key = {
        'id': 'my_id'
    }

    value = {
        "data": [],
        "timestamp": int(NOW.timestamp()*1000)
    }

    producer.poll(0)
    producer.produce(
        KAFKA_TOPIC,
        json.dumps(value),
        json.dumps(key),
        on_delivery=delivery_callback
    )

    producer.flush()
    return


t1 = PythonOperator(
    task_id="main",
    python_callable=main,
    dag=dag
)
