CREATE TABLE IF NOT EXISTS bronze_orders (
    order_id INTEGER,
    customer_id INTEGER,
    product_name VARCHAR(100),
    quantity INTEGER,
    amount NUMERIC(10,2),
    order_date DATE,
    ingestiion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);