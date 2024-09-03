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

# Mean
mean_values = df.mean(numeric_only=True)

# Median
median_values = df.median(numeric_only=True)

# Mode
mode_values = df.mode().iloc[0] if not df.mode().empty else None

# Standard Deviation
std_values = df.std(numeric_only=True)

# Print Descriptive Statistics
print("Mean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nMode:\n", mode_values)
print("\nStandard Deviation:\n", std_values)

OUTPUT:

Mean:
 TransactionID           1050.500000
CustomerID              1516.633333
SalesPersonID             13.890000
QuantitySold               4.610000
UnitPrice                576.215300
TotalSale               2635.582900
Discount                   9.722700
FinalPrice              2624.890700
CustomerSatisfaction       3.120000
dtype: float64

Median:
 TransactionID           1050.500000
CustomerID              1516.633333
SalesPersonID             13.500000
QuantitySold               4.500000
UnitPrice                596.525000
TotalSale               2113.485000
Discount                  10.065000
FinalPrice              2108.580000
CustomerSatisfaction       3.000000
dtype: float64

Mode:
 TransactionID                  1001
StoreID                          D4
ProductID                       M03
CustomerID              1516.633333
SalesPersonID                  12.0
DateOfSale               2023-09-21
QuantitySold                    5.0
UnitPrice                    109.75
TotalSale                    110.94
Discount                        0.0
FinalPrice                   100.66
PaymentMethod                  Cash
Warranty                         No
CustomerSatisfaction            5.0
ReturnStatus               Returned
Name: 0, dtype: object

Standard Deviation:
 TransactionID             29.011492
CustomerID               248.795744
SalesPersonID              2.619449
QuantitySold               2.481833
UnitPrice                282.274886
TotalSale               1995.564776
Discount                   6.499598
FinalPrice              1995.323101
CustomerSatisfaction       1.451436
dtype: float64

