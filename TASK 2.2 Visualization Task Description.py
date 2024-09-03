import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the cleaned dataset
file_path = '/content/mobile_sales_data.csv'
df = pd.read_csv(file_path)

# Ensure numeric columns are in correct type and handle missing values
df['QuantitySold'] = pd.to_numeric(df['QuantitySold'], errors='coerce')
df['FinalPrice'] = pd.to_numeric(df['FinalPrice'], errors='coerce')

df['QuantitySold'].fillna(df['QuantitySold'].median(), inplace=True)
df['FinalPrice'].fillna(df['FinalPrice'].median(), inplace=True)


# Visualization

# 1. Histogram for Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['QuantitySold'], bins=10, kde=True)
plt.title('Distribution of Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Frequency')
plt.show()

# 2. Boxplot for Outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['FinalPrice'])
plt.title('Boxplot of Final Price')
plt.xlabel('Final Price')
plt.show()

# 3. Bar Plot for Categorical Data
plt.figure(figsize=(10, 6))
sns.countplot(x=df['PaymentMethod'])
plt.title('Frequency of Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.show()



