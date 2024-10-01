from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'owner': 'airflow',
}

with DAG(
    dag_id='spark_dag',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False
) as dag:

    spark_submit_task = SparkSubmitOperator(
        task_id='spark_submit_job',
        application='/home/spark/read_csv.py', 
        conn_id='spark_default',  
        verbose=True
    )

    spark_submit_task

