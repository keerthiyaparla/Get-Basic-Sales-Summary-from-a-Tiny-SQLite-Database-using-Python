## 📌 Project Description
This project demonstrates how to use **SQLite**, a lightweight, serverless database, with Python to store, query, and analyze sales data. SQLite stores all data in a single file, making it portable and easy to use without requiring a separate server installation. Python includes built-in SQLite support via the `sqlite3` module, allowing you to work with databases directly from your scripts.

In this project, we:
1. Create a SQLite database file (`sales_data.db`) and a table named `sales`.
2. Insert a dataset containing products, quantities, and prices.
3. Run SQL queries to calculate:
   - **Total Quantity Sold** per product
   - **Total Revenue** per product
4. Identify the product with the **highest revenue**.
5. Visualize the revenue by product using a bar chart with **matplotlib**.

---

## 🛠 Tools & Libraries Used
- **Python 3.12**
- **SQLite** (`sqlite3` module)
- **pandas** – for data manipulation
- **matplotlib** – for data visualization

---

## 📂 Files in This Project
- `task7_sales_summary.py` → Main Python script
- `sales_data.db` → SQLite database file
- `sales_chart.png` → Generated bar chart
- `README.md` → Project documentation

---

## 🚀 How to Run
1. **Install dependencies**:
   ```bash
   python -m pip install pandas matplotlib
