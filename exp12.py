import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 300, 280, 350]
expenses = [150, 200, 220, 210, 260]

# ---------------- LINE GRAPH ----------------
plt.figure()
plt.plot(months, sales, marker='o', label="Sales")
plt.plot(months, expenses, marker='s', label="Expenses")

plt.title("Monthly Sales vs Expenses")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.grid()
plt.show()


# ---------------- BAR CHART ----------------
plt.figure()
plt.bar(months, sales, label="Sales")
plt.bar(months, expenses, bottom=sales, label="Expenses")

plt.title("Monthly Total Revenue")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.show()


# ---------------- PIE CHART ----------------
plt.figure()
plt.pie(sales, labels=months, autopct='%1.1f%%')

plt.title("Sales Distribution by Month")
plt.show()