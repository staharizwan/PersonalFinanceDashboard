#%%
import sqlite3
import pandas as pd

#%% Load processed data
df = pd.read_csv("../data/processed/transactions_clean.csv")
df.head()


# %% Creating a db
conn = sqlite3.connect("../data/spendscope.db")

# %% Loading the data into the db
df.to_sql(
    "transactions",
    conn,
    if_exists = "replace",
    index = False
)

# %%
query = """
    SELECT * FROM transactions LIMIT 5;
"""
pd.read_sql_query(query, conn)

#%%
query = """
    SELECT COUNT(*) AS transaction_count FROM transactions;
"""
pd.read_sql_query(query, conn)

# %%
#conn.close()

# %% Total spending
query = """
    SELECT ROUND(SUM(amount), 2) AS total_spending
    FROM transactions;
    """
pd.read_sql_query(query, conn)

# %% Spending by category
query = """
    SELECT
    category, COUNT(*) AS transactions,
    ROUND(SUM(amount), 2) AS total_spending,
    ROUND(AVG(amount), 2) AS avg_transaction
    FROM transactions
    GROUP BY category
    ORDER BY total_spending DESC;
"""
pd.read_sql_query(query, conn)

# %%
query = """
    PRAGMA table_info(transactions)
"""

pd.read_sql_query(query, conn)
# %%
