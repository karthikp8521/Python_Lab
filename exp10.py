import pandas as pd

# Sample dataset
data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Sales", "IT"],
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Salary": [50000, 40000, 55000, 42000, 45000, 48000, 60000]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# ----------------------------
# Group by Department
# ----------------------------
grouped = df.groupby("Department")

# Aggregate metrics
result = grouped["Salary"].agg(["count", "sum", "mean", "min", "max"])

print("\nAggregated Data:\n", result)