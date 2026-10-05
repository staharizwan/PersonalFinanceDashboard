-- 
SELECT is_weekend,
        ROUND(SUM(amount), 2) AS total_spending,
        COUNT(*) AS transaction_count,
        ROUND(AVG(amount), 2) AS average_transaction
        FROM transactions
        GROUP BY is_weekend
        ORDER BY total_spending;

--
SELECT
    date,
    DATE(date) AS calendar_date
FROM transactions
LIMIT 10;