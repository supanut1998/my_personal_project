from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow'
}

# Define the DAG
dag = DAG(
    'spark_submit_test_dag',
    default_args=default_args,
    description='A simple test DAG to submit Spark jobs',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# Define the SparkSubmitOperator task
submit_spark_job = SparkSubmitOperator(
    task_id='submit_spark_job',
    application='/opt/airflow/dags/repo/dags/spark-file.py',  # Path to your Spark application
    conn_id='spark_default',  # Connection ID for Spark
    executor_cores=2,
    executor_memory='2g',
    num_executors=2,
    driver_memory='1g',
    name='airflow-spark-test-job',
    dag=dag,
)

# Set the task in the DAG
submit_spark_job
