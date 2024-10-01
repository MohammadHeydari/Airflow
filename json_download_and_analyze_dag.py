from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import json

def download_json():
    url = 'https://jsonplaceholder.typicode.com/posts'  # URL واقعی JSON
    response = requests.get(url)
    with open('/root/airflow/dags/data.json', 'w') as f:
        f.write(response.text)

def analyze_data():
    with open('/root/airflow/dags/data.json', 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    
    post_count = df.shape[0]
    
    df['title_length'] = df['title'].apply(len)
    avg_title_length = df['title_length'].mean()
    
    print(f"Total Posts: {post_count}")
    print(f"Average Title Length: {avg_title_length:.2f}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG('json_download_and_analyze_dag', default_args=default_args, schedule_interval='@once')

download_task = PythonOperator(
    task_id='download_json',
    python_callable=download_json,
    dag=dag,
)

analyze_task = PythonOperator(
    task_id='analyze_data',
    python_callable=analyze_data,
    dag=dag,
)

download_task >> analyze_task

