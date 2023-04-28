import py
from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta
from etl_function.etl_helper import *
url_env = Variable.get('url')


default_args = {
    'owner': 'Supanut Onsri'
}

dag = DAG(dag_id='etl_pipeline', 
default_args=default_args, 
start_date=days_ago(1), 
schedule_interval=None)

extract_task = PythonOperator(
    task_id='extract', 
    python_callable=ingest, 
    op_kwargs={'url_data':url_env},
    dag=dag
)

transfrom_task = PythonOperator(
    task_id='transform', 
    python_callable=transfrom, 
    op_kwargs={'file_json':'data/data.json'}, 
    dag=dag
)

load_task = BashOperator(
    task_id='load', 
    bash_command='cp -r /opt/airflow/data/conversion_rate.csv /opt/airflow/output', 
    dag=dag
)

extract_task >> transfrom_task >> load_task