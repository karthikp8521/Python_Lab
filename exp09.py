import pandas as pd

# Sales DataFrame
sales = pd.DataFrame({
    "ProductID": [101, 102, 103, 104],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Amount": [50000, 20000, 30000, 15000]
})

# Customer Orders DataFrame
orders = pd.DataFrame({
    "ProductID": [101, 102, 105],
    "Customer": ["Ravi", "Anu", "Kiran"],
    "City": ["Hyderabad", "Chennai", "Mumbai"]
})

print("Sales Data:\n", sales)
print("\nOrders Data:\n", orders)

# ---------------- INNER JOIN ----------------
inner_join = pd.merge(sales, orders, on="ProductID", how="inner")
print("\nInner Join:\n", inner_join)

# ---------------- LEFT JOIN ----------------
left_join = pd.merge(sales, orders, on="ProductID", how="left")
print("\nLeft Join:\n", left_join)

# ---------------- OUTER JOIN ----------------
outer_join = pd.merge(sales, orders, on="ProductID", how="outer")
print("\nOuter Join:\n", outer_join)