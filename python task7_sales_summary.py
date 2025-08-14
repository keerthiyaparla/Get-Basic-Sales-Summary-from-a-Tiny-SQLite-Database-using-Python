import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Create/connect to the SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# 2️⃣ Create the sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3️⃣ New sample dataset (realistic products)
sales_data = [
    ("Laptop", 5, 60000),
    ("Smartphone", 8, 35000),
    ("Tablet", 4, 25000),
    ("Monitor", 3, 15000),
    ("Keyboard", 10, 1500),
    ("Mouse", 15, 500),
    ("Printer", 2, 18000),
    ("Headphones", 12, 2000),
    ("Smartwatch", 6, 12000),
    ("External HDD", 5, 4500),
    ("USB Drive", 20, 800),
    ("Camera", 3, 55000)
]

# 4️⃣ Clear table and insert new data
cursor.execute("DELETE FROM sales")
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", sales_data)
conn.commit()

# 5️⃣ Query for total quantity and revenue
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# 6️⃣ Print results
print("\nSales Summary:")
print(df)

# 7️⃣ Find highest revenue product
max_row = df.loc[df['revenue'].idxmax()]
print(f"\nHighest revenue: {max_row['product']} with ₹{max_row['revenue']}")

# 8️⃣ Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['product'], df['revenue'], color="skyblue")

# Highlight highest revenue bar in red
bars[df['revenue'].idxmax()].set_color('red')

plt.title("Revenue by Product", fontsize=16)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Revenue (₹)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# 9️⃣ Close connection
conn.close()
