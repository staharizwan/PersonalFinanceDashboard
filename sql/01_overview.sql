-- Overview
SELECT 
    SUM(amount) AS total_spending, 
    COUNT(*) AS transaction_count, 
    ROUND(AVG(amount), 2) AS average_transaction, 
    MAX(amount) AS largest_transaction

FROM transactions;

-- Aggregation by year
SELECT
    year,
    ROUND(SUM(amount), 2) AS total_spending,
    COUNT(*) AS transaction_count,
    ROUND(AVG(amount),2) AS average_transaction
FROM transactions
GROUP BY year
ORDER BY year;


