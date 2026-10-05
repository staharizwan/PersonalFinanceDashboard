-- Monthly trends
SELECT
    year_month,
    ROUND(SUM(amount), 2) as total_spending,
    COUNT(*) AS transaction_count,
    ROUND(AVG(amount), 2) as average_transaction
FROM transactions
GROUP BY year_month
ORDER BY year_month DESC;



-- Month over month spending analysis by using the CTE
WITH monthly_spending AS (
    SELECT year_month,
    ROUND(SUM(amount), 2) AS total_spending
    FROM transactions
    GROUP BY year_month
    )

SELECT
    year_month,
    total_spending,
    LAG(total_spending) OVER (
        ORDER BY year_month
    ) AS previous_month_spending
FROM monthly_spending
ORDER BY year_month;

-- Chaining CTEs together
WITH monthly_spending AS (
    SELECT year_month,
    ROUND(SUM(amount), 2) AS total_spending
    FROM transactions
    GROUP BY year_month
    ),

monthly_comparison AS (
    SELECT year_month,
    total_spending,
    LAG(total_spending) OVER (
        ORDER BY year_month
    ) AS previous_monthly_spending
    FROM monthly_spending)

SELECT year_month,
    total_spending,
    previous_monthly_spending,
    ROUND(
        total_spending - previous_monthly_spending) AS spending_change,
    ROUND(((total_spending - previous_monthly_spending)/(previous_monthly_spending))*100, 2) AS percentage_change
    
    FROM monthly_comparison
    ORDER BY year_month;

