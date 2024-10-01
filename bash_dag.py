from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG('bash_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    task_1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    task_2 = BashOperator(
        task_id='show_current_directory',
        bash_command='pwd'
    )

    task_3 = BashOperator(
        task_id='list_files',
        bash_command='ls -l'
    )

    task_1 >> task_2 >> task_3

