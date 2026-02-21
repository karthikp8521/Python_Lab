import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset (built-in dataset)
df = sns.load_dataset("iris")

print(df.head())

# ---------------- HEATMAP ----------------
plt.figure(figsize=(6,4))
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()


# ---------------- PAIR PLOT ----------------
sns.pairplot(df, hue="species", markers=["o","s","D"])
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()


# ---------------- REGRESSION PLOT ----------------
plt.figure(figsize=(6,4))
sns.regplot(x="sepal_length", y="petal_length", data=df, scatter_kws={"s":50})
plt.title("Regression Plot: Sepal vs Petal Length")
plt.show()