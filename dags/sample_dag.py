import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["teste@teste.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

def sample_function():
    print("This example is running successfully")

with DAG(
    dag_id="sample_dag",
    default_args=default_args,
    description="Tutorial: How make and run a DAG",
    schedule_interval="0 6 * * *",
    start_date=pendulum.datetime(2024, 1, 4, tz="America/Sao_Paulo"),
    tags=["sample", "example"],
    catchup=False,
) as dag:

    sample_task = PythonOperator(
        task_id="sample_task",
        python_callable=sample_function,
    )

    (
        sample_task
    )
