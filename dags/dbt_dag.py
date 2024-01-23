from pendulum import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from cosmos.providers.dbt.task_group import DbtTaskGroup

with DAG(
    dag_id="sample_dbt",
    start_date=datetime(2024, 1, 5),
    schedule="@daily",
) as dag:
    
    init = EmptyOperator(task_id="init")

    workflow = DbtTaskGroup(
        group_id="workflow",
        dbt_project_name="sample_dbt",
        conn_id="db_dbt",
        dbt_root_path="/home/ericsonmatheus/personal/astronomer-cosmos/dags/dbt",
        dbt_args={
            "schema": "public",
        }
    )

    finish = EmptyOperator(task_id="finish")

    init >> workflow >> finish