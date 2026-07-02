CREATE TABLE IF NOT EXISTS gold_daily_revenue (
    order_date DATE PRIMARY KEY,
    total_revenue NUMERIC(12,2),
    total_orders INTEGER,
    updated_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);