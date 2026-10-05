#%%
import pandas as pd

#%% 
df = pd.read_csv("../data/11 march 2025.csv")

# %% Converting date to datetime
df["date"] = pd.to_datetime(df["date"], utc = True)

# %%
df.info()

# %%
df["date"].max(), df["date"].min()

# %% Cleaning category names
category_mapping = {
    "joy" : "Joy",
    "Restuarant" : "Restaurant",
    "business_expenses" : "Business Expenses",
    "Coffe" : "Coffee"
}
df["category"] = df["category"].replace(category_mapping)

# %%
df["category"].unique()

# %% Checking for invalid amounts
(df["amount"] <= 0).sum()

# %% Checking for NA
(df["amount"].isna()).sum()

# %%
df["category"].value_counts()



# %% Feature engineering - date components
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.day_name()
df["hour"] = df["date"].dt.hour


# %%
df.head()

# %%
df["year_month"] = df["date"].dt.to_period("M").astype(str)

# %%
df[["date", "year_month"]].head()

# %% Weekend indicator
df["is_weekend"] = df["date"].dt.day_of_week >= 5

# %%
df.head()

# %%
#%%
df[["year", "month", "month_name", "weekday", "hour", "year_month", "is_weekend"]].head(10)
# %%

#%% Final validation
print("Rows:", len(df))
print("Missing values:", df.isna().sum().sum())
print("Duplicates:", df.duplicated().sum())
print("Min date:", df["date"].min())
print("Max date:", df["date"].max())
print("Categories:", df["category"].nunique())

# %% Saving the cleaned df
output_path = "../data/processed/transactions_clean.csv"
df.to_csv(output_path, index = False)
print(f"Saved {len(df)} rows to {output_path}")

# %%
