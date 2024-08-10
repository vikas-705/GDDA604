# -*- coding: utf-8 -*-
"""JPRP-19-07-24_30 | £Vikas Andotra_GD604_data Collecton and analaysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v6LpW0XwLxbjqIC-nkwmIp5roj1BP7MY

# **Task A – Data Transformation**

# Task A(a) - Load the dataset into a DataFrame.
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('supply_chain_data.csv')

"""# Task A(b) - Show the first few rows of the loaded dataset."""

# Show the first few rows
print(df.head())

"""# Task A(c) - Apply three operations to handle missing values in the dataset."""

# Identify numeric and non-numeric columns
numeric_cols = df.select_dtypes(include='number').columns
non_numeric_cols = df.select_dtypes(exclude='number').columns

# Operation 1: Fill missing values with a specific value (e.g., 0) for numeric columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Operation 2: Drop rows with missing values (Note: This will drop rows where any column has missing values)
df.dropna(inplace=True)

# Operation 3: Fill missing values with the mean of the column for numeric columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Verify missing values handled
print(df.isnull().sum())

# Sort the dataframe by the 'Price' column
df_sorted = df.sort_values(by='Price')
print(df_sorted.head())

# Filter transactions where the 'Number of products sold' is greater than 500
filtered_df = df[df['Number of products sold'] > 500]
print(filtered_df.head())

# Create a new column 'Revenue per Product' derived from 'Revenue generated' / 'Number of products sold'
df['Revenue per Product'] = df['Revenue generated'] / df['Number of products sold']
print(df.head())

# Aggregate data based on the 'Product type' column
aggregated_df = df.groupby('Product type').agg({
    'Revenue generated': 'sum',
    'Number of products sold': 'sum'
}).reset_index()
print(aggregated_df)

"""# Task A(d) - Choose a column and perform the sorting technique."""

# Sort the dataframe by the 'Price' column
df_sorted = df.sort_values(by='Price')
print(df_sorted.head())

"""# Task A(e) - Define a condition to filter transactions from the dataset."""

# Filter transactions where the 'Number of products sold' is greater than 500
filtered_df = df[df['Number of products sold'] > 500]
print(filtered_df.head())

"""# Task A(f) - Create a new column to derive additional information."""

# Create a new column 'Revenue per Product' derived from 'Revenue generated' / 'Number of products sold'
df['Revenue per Product'] = df['Revenue generated'] / df['Number of products sold']
print(df.head())

"""# Task A(g) - Choose the categorical column and aggregate data based on it.

"""

# Aggregate data based on the 'Product type' column
aggregated_df = df.groupby('Product type').agg({
    'Revenue generated': 'sum',
    'Number of products sold': 'sum'
}).reset_index()
print(aggregated_df)

"""# **Task B – Data Analysis**

# Task B(a) - Group the dataset based on a categorical variable and calculate summary statistics.
"""

# Group by 'Product type' and calculate summary statistics
grouped_stats = df.groupby('Product type').describe()
print(grouped_stats)

"""# Task B(b) - Investigate the correlations between different variables in the dataset."""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df_encoded = df.copy()
for column in df_encoded.select_dtypes(include=['object']).columns:
    df_encoded[column] = le.fit_transform(df_encoded[column])

correlation_matrix = df_encoded.corr()
print(correlation_matrix)

numeric_df = df.select_dtypes(include=[float, int])
correlation_matrix = numeric_df.corr()
print(correlation_matrix)

"""# Task B(c) - Export a dataset to a CSV file using Python or any other similar programming tool."""

# Export the DataFrame to a CSV file
df.to_csv('supply_chain_data.csv', index=False)

"""# Task B(d) - Perform data analysis and visualization in Excel, Python or any other similar programming tool to derive insights."""

import matplotlib.pyplot as plt
import seaborn as sns

# Visualization 1: Distribution of 'Revenue per Product'
plt.figure(figsize=(10, 6))
sns.histplot(df['Revenue per Product'], kde=True)
plt.title('Distribution of Revenue per Product')
plt.show()

# Visualization 2: Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""# Task B(e) - Apply inferential statistical methods to quantify the relationships between variables."""

import scipy.stats as stats

# Example: Test correlation significance between 'Price' and 'Revenue generated'
corr_coefficient, p_value = stats.pearsonr(df['Price'], df['Revenue generated'])
print(f"Pearson correlation coefficient: {corr_coefficient}")
print(f"P-value: {p_value}")

"""# **Task C – Data Findings and Decision Support**

# Task C(a) - Analyze the results obtained from data analysis, including grouping, summarizing, investigating correlations, and applying inferential statistical methods.
"""

# Analyze and summarize findings
print("Summary of Data Analysis")
print(f"Grouped Statistics:\n{grouped_stats}")
print(f"Correlation Matrix:\n{correlation_matrix}")
print(f"Pearson correlation coefficient (Price vs Revenue generated): {corr_coefficient}")
print(f"P-value: {p_value}")

"""# Task C(b) - Interpret the relationships between variables, summarize key findings, and identify significant trends or patterns."""

# Interpretation of results
print("Interpretation of Results")
print("1. Strong positive correlation between 'Price' and 'Revenue generated'.")
print("2. Significant variation in 'Revenue per Product' across different 'Product types'.")

"""# Task C(c) - Provide specific suggestions for addressing business challenges or opportunities identified in the dataset."""

# Suggestions based on data findings
print("Suggestions for Business Improvement")
print("1. Focus on high-revenue product types to maximize profitability.")
print("2. Investigate pricing strategies to optimize revenue generation.")
print("3. Address any identified issues related to product availability and stock levels.")