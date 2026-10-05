-- Expedenditure by category
SELECT
    category,  
    ROUND(SUM(amount), 2) as total_spending,
    COUNT(*) as transaction_count,
    ROUND(AVG(amount), 2) as average_transaction
FROM transactions
GROUP BY category
ORDER BY total_spending DESC;

-- Window function; checking the spending %
SELECT 
    category,
    SUM(amount) AS total_spending,
    ROUND(SUM(amount) * 100 / SUM(SUM(amount)) OVER(), 2) AS spending_percentage
FROM transactions
GROUP BY category
ORDER BY total_spending DESC;