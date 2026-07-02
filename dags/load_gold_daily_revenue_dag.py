from datetime import datetime

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="load_gold_revenue",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    template_searchpath=["/opt/airflow/sql"],
    tags=["project1", "gold"],
) as dag:

    load_gold = SQLExecuteQueryOperator(
        task_id="load_gold",
        conn_id="warehouse_postgres",
        sql="load_gold_daily_revenue.sql",
    )

