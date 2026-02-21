import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix, lag_plot, autocorrelation_plot
import numpy as np

# Create time-series dataset
np.random.seed(0)
dates = pd.date_range(start="2024-01-01", periods=50)
values = np.cumsum(np.random.randn(50))  # cumulative random walk

df = pd.DataFrame({
    "Date": dates,
    "Sales": values,
    "Advertising": values + np.random.randn(50)*2,
    "Profit": values + np.random.randn(50)*1.5
})

df.set_index("Date", inplace=True)

print(df.head())

# ---------------- Scatter Matrix ----------------
plt.figure()
scatter_matrix(df, figsize=(8,8))
plt.suptitle("Scatter Matrix")
plt.show()

# ---------------- Lag Plot ----------------
plt.figure()
lag_plot(df["Sales"])
plt.title("Lag Plot (Sales)")
plt.show()

# ---------------- Autocorrelation Plot ----------------
plt.figure()
autocorrelation_plot(df["Sales"])
plt.title("Autocorrelation Plot (Sales)")
plt.show()