from datetime import datetime

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


with DAG(
    dag_id="load_silver_orders",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    template_searchpath=["/opt/airflow/sql"],
    tags=["project1", "silver"],
) as dag:

    load_silver = SQLExecuteQueryOperator(
        task_id="load_silver",
        conn_id="warehouse_postgres",
        sql="load_silver_orders.sql",
    )