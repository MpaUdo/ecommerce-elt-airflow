from datetime import datetime

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


default_args = {
    "owner": "mpaudo",
}


with DAG(
    dag_id="setup_warehouse",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    template_searchpath=["/opt/airflow/sql"],
    tags=["project1"],
) as dag:

    create_bronze = SQLExecuteQueryOperator(
        task_id="create_bronze",
        conn_id="warehouse_postgres",
        sql="create_bronze.sql",
    )

    create_silver = SQLExecuteQueryOperator(
        task_id="create_silver",
        conn_id="warehouse_postgres",
        sql="create_silver.sql",
    )

    create_gold = SQLExecuteQueryOperator(
        task_id="create_gold",
        conn_id="warehouse_postgres",
        sql="create_gold.sql",
    )

    create_bronze >> create_silver >> create_gold