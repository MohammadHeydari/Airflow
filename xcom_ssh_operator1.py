
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

default_args = {
    'start_date': days_ago(1),
}

def process_xcom_data(**kwargs):
    # Pull the data stored in XCom from previous task
    ti = kwargs['ti']
    xcom_data = ti.xcom_pull(key='return_value', task_ids='extract_via_ssh')

    print(f"Processing data from XCom: {xcom_data}")

    # Do the necessary processing with the pulled data (for example logging)
    process_type = kwargs['dag_run'].conf.get('process_type', 'cleaning')
    print(f"Processing with type: {process_type}")

with DAG(
    'xcom_ssh_operator1',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    # Task to extract data via SSH
    extract_via_ssh = SSHOperator(
        task_id='extract_via_ssh',
        ssh_conn_id='my_ssh_connection',  # Define your SSH connection in Airflow
        command="cat /home/dataset/data/flight-data/csv/2015-summary.csv",  # Command that fetches data
        do_xcom_push=True,  # To store the output of the SSH command in XCom
    )

    # Task to process the data pulled from XCom
    process_data_task = PythonOperator(
        task_id='process_data_task',
        python_callable=process_xcom_data,
        provide_context=True,
    )

    extract_via_ssh >> process_data_task

