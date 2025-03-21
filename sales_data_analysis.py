 
import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\sales archive.zip", encoding="ISO-8859-1")

# Convert dates to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# 1. Overview of Sales Data
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
top_category = df.groupby("Category")["Sales"].sum().idxmax()

# 2. Top 5 Customers by Sales
top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(5)

# 3. Best-Selling Products
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(5)

# 4. Sales by Region
sales_by_region = df.groupby("Region")["Sales"].sum()

# Print results
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Best-Selling Category: {top_category}")
print("\nTop 5 Customers:\n", top_customers)
print("\nTop 5 Products:\n", top_products)
print("\nSales by Region:\n", sales_by_region)
