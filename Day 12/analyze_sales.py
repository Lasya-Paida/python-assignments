import pandas as pd

df = pd.read_csv("Day 12/sales_data.csv")

print("Original Data:")
print(df)

df_clean = df.dropna()
df_clean["Units Sold"] = df_clean["Units Sold"].astype(int)

df_clean["Revenue"] = df_clean["Units Sold"] * df_clean["Unit Price"]

df_sorted = df_clean.sort_values(by=["Date", "Region"])

summary = df_sorted.groupby("Region")["Revenue"].sum().reset_index()

print("\nCleaned & Sorted Data:")
print(df_sorted)

print("\nRevenue Summary by Region:")
print(summary)

df_sorted.to_csv("Day 12/cleaned_sales_data.csv", index=False)
summary.to_csv("Day 12/revenue_summary.csv", index=False)

print("\nFiles saved: cleaned_sales_data.csv and revenue_summary.csv")