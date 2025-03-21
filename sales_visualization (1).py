 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\DELL\\OneDrive\\Documents\\sales archive.zip", encoding="ISO-8859-1")

# Convert dates to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Set seaborn style
sns.set(style="whitegrid")

# 1. Sales by Category
plt.figure(figsize=(8, 5))
category_sales = df.groupby("Category")["Sales"].sum().sort_values()
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.xlabel("Total Sales ($)")
plt.ylabel("Category")
plt.title("Total Sales by Category")
plt.show()

# 2. Profit Trend Over Time
df.sort_values("Order Date", inplace=True)
df["Year-Month"] = df["Order Date"].dt.to_period("M")
monthly_profit = df.groupby("Year-Month")["Profit"].sum()

plt.figure(figsize=(10, 5))
monthly_profit.plot(marker="o", linestyle="-", color="b")
plt.xlabel("Month")
plt.ylabel("Total Profit ($)")
plt.title("Profit Trend Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Top 5 Selling Products
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(5)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="coolwarm")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.title("Top 5 Selling Products")
plt.show()
