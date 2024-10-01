from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG('hello_world', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')
    hello_operator = PythonOperator(task_id='say_hello', python_callable=print_hello)
    start >> hello_operator

