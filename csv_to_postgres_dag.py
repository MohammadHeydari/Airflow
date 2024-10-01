from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_postgres():
    df = pd.read_csv('/root/airflow/dags/data.csv')

    engine = create_engine('postgresql://postgres@localhost/test_db')

    df.to_sql('data_table', con=engine, if_exists='append', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('csv_to_postgres_dag', default_args=default_args, schedule_interval='@once')

load_data_task = PythonOperator(
    task_id='load_csv_to_postgres',
    python_callable=load_csv_to_postgres,
    dag=dag,
)

