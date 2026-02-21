import pandas as pd

# Load CSV file
df = pd.read_csv("Python/data.csv")

print("\nOriginal Data:\n", df)

# ----------------------------
# Check missing values
# ----------------------------
print("\nMissing Values:\n", df.isnull().sum())

# ----------------------------
# Fill missing numeric values with mean
# ----------------------------
for col in df.select_dtypes(include=['float64','int64']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ----------------------------
# Rename columns
# ----------------------------
df.rename(columns={
    df.columns[0]: "ID",
    df.columns[1]: "Name",
    df.columns[2]: "Value"
}, inplace=True)

print("\nCleaned Data:\n", df)

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved as cleaned_data.csv")