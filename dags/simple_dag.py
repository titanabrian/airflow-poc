from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from tasks.simple_program import run

args = {
  'owner': 'titanabrian',
  'start_date': days_ago(1)
}

dag = DAG(
  dag_id='simple-dag',
  default_args=args,
  schedule_interval='@daily'
)

with dag:
  run = PythonOperator(
    task_id='simple-task',
    python_callable=run,
  )