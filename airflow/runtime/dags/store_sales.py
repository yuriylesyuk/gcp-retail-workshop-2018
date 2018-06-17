import os
from datetime import datetime, timedelta

from airflow import DAG
# from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.operators.bash_operator import BashOperator

airflow_home = os.environ.get('AIRFLOW_HOME')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 6, 16),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('bq_stores_sales_processing',
          schedule_interval=None,
          catchup=False,
          default_args=default_args)

bq_store_sales_task = BashOperator(task_id='bq_store_sales_bash',
                                   bash_command='bq query --use_legacy_sql=False < ' + airflow_home + '/scripts/store_sales.sql ',
                                   dag=dag)

# bq_store_sales_task = BigQueryOperator(
#     task_id='bq_store_sales',
#     bql=airflow_home + '/scripts/store_sales.sql',
#     bigquery_conn_id='google_cloud_default',
#     use_legacy_sql=False,
#     delegate_to='airflow@{GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com',
#     dag=dag)
