import pandas as pd

df = pd.read_excel("Cleaned dataset.xlsx")

print("First 5 rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

#Basic static analysis
print("\nMean: ")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].mean())

print("\nMedian: ")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].median())

print("\nCount: ")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].count())


import matplotlib.pyplot as plt

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove rows where Date is missing or invalid
trend_df = df.dropna(subset=["Date"]).copy()

# Calculate monthly total price
trend_df["Month"] = trend_df["Date"].dt.to_period("M")

monthly_trend = trend_df.groupby("Month")["TotalPrice"].sum()

print("\n--- Monthly Trend ---")
print(monthly_trend)

# Plot the trend
monthly_trend.index = monthly_trend.index.astype(str)

plt.figure(figsize=(12, 5))
plt.plot(monthly_trend.index, monthly_trend.values, marker="o")
plt.title("Monthly Total Price Trend")
plt.xlabel("Month")
plt.ylabel("Total Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Step 4: Outlier Detection using IQR

print("\n--- Outlier Detection ---")

columns = ["Quantity", "UnitPrice", "TotalPrice"]

for col in columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit)
    ]

    # Print results
    print(f"\nColumn: {col}")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Potential Outliers:", len(outliers))

    if not outliers.empty:
        print("Outlier Values:")
        print(outliers[col].to_list())

        print("\nOutlier Records:")
        print(outliers)
    else:
        print("No outliers found.")


# Step 5: Key Observations

print("\n--- Key Observations ---")

# 1. Total number of orders
print("Total Orders:", len(df))

# 2. Average order quantity
print("Average Quantity:", round(df["Quantity"].mean(), 2))

# 3. Average unit price
print("Average Unit Price:", round(df["UnitPrice"].mean(), 2))

# 4. Average total price
print("Average Total Price:", round(df["TotalPrice"].mean(), 2))

# 5. Highest and lowest total price
print("Highest Total Price:", df["TotalPrice"].max())
print("Lowest Total Price:", df["TotalPrice"].min())

# 6. Most common product
print("Most Common Product:", df["Product"].mode()[0])

# 7. Orders by status
print("\nOrders by Status:")
print(df["OrderStatus"].value_counts())

# 8. Highest monthly total price
print("\nHighest Monthly Total Price:")
print(monthly_trend.idxmax(), "=", monthly_trend.max())

# 9. Lowest monthly total price
print("\nLowest Monthly Total Price:")
print(monthly_trend.idxmin(), "=", monthly_trend.min())

