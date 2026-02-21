import numpy as np
import pandas as pd

# Create NumPy array
data = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [12, 22, 32],
    [18, 28, 38]
])

print("NumPy Array:\n", data)

# Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=["Maths", "Physics", "Chemistry"])

print("\nDataFrame:\n", df)

# Basic statistics
print("\n--- Statistics ---")
print("Mean:\n", df.mean())
print("\nMedian:\n", df.median())
print("\nStandard Deviation:\n", df.std())
print("\nMinimum:\n", df.min())
print("\nMaximum:\n", df.max())