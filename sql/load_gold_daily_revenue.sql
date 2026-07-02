TRUNCATE TABLE gold_daily_revenue;

INSERT INTO gold_daily_revenue (
    order_date,
    total_orders,
    total_revenue
)

SELECT
    order_date,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_revenue
FROM silver_orders
GROUP BY order_date
ORDER BY order_date;