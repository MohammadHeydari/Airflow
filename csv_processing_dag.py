from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def process_csv():
    df = pd.read_csv('/root/airflow/dags/input_data.csv')

    df['age'] -= 1

    df.to_csv('/root/airflow/dags/output_data.csv', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('csv_processing_dag', default_args=default_args, schedule_interval='@once')

process_csv_task = PythonOperator(
    task_id='process_csv',
    python_callable=process_csv,
    dag=dag,
)

