from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def write_file():
    with open('/root/airflow/dags/sample_file.txt', 'w') as f:
        f.write('Hello, Haji!, Whats Up Dadash...')

def read_file():
    with open('/root/airflow/dags/sample_file.txt', 'r') as f:
        content = f.read()
        print(content)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('read_write_dag', default_args=default_args, schedule_interval='@once')

task1 = PythonOperator(
    task_id='write_file',
    python_callable=write_file,
    dag=dag,
)

task2 = PythonOperator(
    task_id='read_file',
    python_callable=read_file,
    dag=dag,
)

task1 >> task2

