#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ===============================
# TASK 1: IRIS EDA & VISUALIZATION
# ===============================

# Step 1: Imports
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load dataset
# Option A: From seaborn built-in
def load_iris_from_seaborn():
    try:
        df = sns.load_dataset('iris')
        print("Loaded iris dataset from seaborn.")
        return df
    except Exception as e:
        print("❌ Failed to load iris from seaborn:", e)
        return None


# Try seaborn first, fallback to CSV
df_iris = load_iris_from_seaborn()
if df_iris is None:
    df_iris = load_iris_from_csv()

if df_iris is None:
    raise SystemExit("Could not load Iris dataset from any source. Check your setup.")

# Step 3: Basic inspection
print("\nShape of dataset:", df_iris.shape)
print("\nColumn names:", df_iris.columns.tolist())

print("\nFirst 5 rows:")
display(df_iris.head())

print("\nInfo:")
print(df_iris.info())

print("\nSummary statistics:")
display(df_iris.describe(include='all'))

# Step 4: Handle basic fail case - check for missing values
missing_counts = df_iris.isna().sum()
print("\nMissing values per column:")
print(missing_counts)

if missing_counts.any():
    print("\n⚠️ Dataset has missing values. For now, we will drop rows with missing data.")
    df_iris = df_iris.dropna()
    print("New shape after dropping missing rows:", df_iris.shape)

# Step 5: Scatter plot – relationships between features
# Example: sepal_length vs sepal_width colored by species
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_iris,
    x=df_iris.columns[0],  # assuming numeric
    y=df_iris.columns[1],  # assuming numeric
    hue=df_iris.columns[-1]  # assuming last col is species
)
plt.title("Scatter Plot of First Two Features Colored by Species")
plt.show()

# Step 6: Histograms for each numeric feature
numeric_cols = df_iris.select_dtypes(include=['float64', 'int64']).columns
df_iris[numeric_cols].hist(figsize=(10, 8), bins=10)
plt.suptitle("Histograms of Numeric Features")
plt.tight_layout()
plt.show()

# Step 7: Box plots to see outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_iris[numeric_cols])
plt.title("Box Plots of Numeric Features")
plt.xticks(rotation=45)
plt.show()

# Step 8: Final text insight 
print("\n EDA completed.")
print("- Differences in feature distributions between species")
print("- Any outliers visible in box plots")
print("- Which features seem most separable visually")


# In[ ]:




