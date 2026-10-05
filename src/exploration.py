#%%
import pandas as pd

#%%
df = pd.read_csv("../data/11 march 2025.csv")

#%%
df.head(50)

# %%
df.shape

# %%
df.info()

#%% Missing values
df.isna().sum()

#%% Duplicate rows
df.duplicated().sum()

#%% Unique categories
df["category"].nunique()

#%% Category distribution
df["category"].value_counts()

#%% Amount statistics
df["amount"].describe()
# %%

#%% Largest transactions
df.nlargest(10, "amount")
# %%

#%% Smallest transactions
df.nsmallest(10, "amount")
# %%

#%% Raw date values
df["date"].head(10)

# %%
df["date"].dtype
# %%
