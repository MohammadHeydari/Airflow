from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def extract_config(**kwargs):
    input_file = kwargs['dag_run'].conf.get('input_file', 'default_file.csv')
    process_type = kwargs['dag_run'].conf.get('process_type', 'cleaning')

    kwargs['ti'].xcom_push(key='input_file', value=input_file)
    kwargs['ti'].xcom_push(key='process_type', value=process_type)

    print(f"Extracted config: input_file={input_file}, process_type={process_type}")

def process_data(**kwargs):
    ti = kwargs['ti']
    input_file = ti.xcom_pull(key='input_file', task_ids='extract_config_task')
    process_type = ti.xcom_pull(key='process_type', task_ids='extract_config_task')

    print(f"Processing file {input_file} with process type {process_type}")

default_args = {
    'start_date': days_ago(1),
}

with DAG(
    'xcom_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    extract_config_task = PythonOperator(
        task_id='extract_config_task',
        python_callable=extract_config,
        provide_context=True,
    )

    process_data_task = PythonOperator(
        task_id='process_data_task',
        python_callable=process_data,
        provide_context=True,
    )

    extract_config_task >> process_data_task

