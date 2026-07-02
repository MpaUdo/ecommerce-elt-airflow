from datetime import datetime
import csv
import psycopg2

from airflow.decorators import dag, task


WAREHOUSE_CONN = {
    "host": "warehouse-postgres",
    "database": "ecommerce_warehouse",
    "user": "warehouse",
    "password": "warehouse",
    "port": 5432,
}


@dag(
    dag_id="load_bronze_orders",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["project1", "bronze"],
)
def load_bronze_orders():

    @task
    def load_csv_to_bronze():
        file_path = "/opt/airflow/data/orders.csv"

        conn = psycopg2.connect(**WAREHOUSE_CONN)
        cur = conn.cursor()

        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO bronze_orders (
                        order_id,
                        customer_id,
                        product_name,
                        quantity,
                        amount,
                        order_date
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        row["order_id"],
                        row["customer_id"],
                        row["product_name"],
                        row["quantity"],
                        row["amount"],
                        row["order_date"],
                    ),
                )

        conn.commit()
        cur.close()
        conn.close()

    load_csv_to_bronze()


load_bronze_orders()