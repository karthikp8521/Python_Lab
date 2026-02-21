import pandas as pd

# Sample dataset
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Marks": [45, 78, 88, 59]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# ----------------------------
# Custom function: Grade assignment
# ----------------------------
def assign_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# Apply to column
df["Grade"] = df["Marks"].apply(assign_grade)

# ----------------------------
# Custom function: Bonus marks (+5)
# ----------------------------
df["Updated Marks"] = df["Marks"].apply(lambda x: x + 5)

print("\nModified Data:\n", df)