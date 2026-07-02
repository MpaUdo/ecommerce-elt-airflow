TRUNCATE TABLE silver_orders;

INSERT INTO silver_orders (
    order_id,
    customer_id,
    product_name,
    quantity,
    amount,
    order_date
)
SELECT
    order_id,
    customer_id,
    product_name,
    quantity,
    amount,
    order_date
FROM (
    SELECT
        order_id,
        customer_id,
        product_name,
        quantity,
        amount,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY ingestion_timestamp DESC
        ) AS rn
    FROM bronze_orders
) t
WHERE rn = 1;