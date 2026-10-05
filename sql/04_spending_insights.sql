-- Top 5 months by spending
SELECT year_month,
ROUND(SUM(amount), 2) AS total_spending
FROM transactions
GROUP BY year_month
ORDER BY total_spending DESC
LIMIT 5;

-- Expenditure by category
SELECT category,
    SUM(amount) AS total_spending,
    COUNT(*) AS transaction_count
    FROM transactions
    WHERE year_month = "2024-07"
    GROUP BY category;


-- Evaluating the spike from July, 2024
SELECT category,
       year_month,
       amount
    FROM transactions
    WHERE year_month = "2024-07" AND category = "Tech"
    ORDER BY amount DESC;