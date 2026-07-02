CREATE TABLE IF NOT EXISTS silver_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name VARCHAR(100),
    quantity INTEGER,
    amount NUMERIC(10,2),
    order_date DATE,
    processed_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
