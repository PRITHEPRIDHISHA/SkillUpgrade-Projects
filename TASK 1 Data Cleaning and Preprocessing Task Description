import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
file_path = '/content/ugly_mobile_sales_data.csv'
df = pd.read_csv(file_path)

# Step 1: Handle Missing Values
# Fill missing numeric values with mean or median
df['CustomerID'].fillna(df['CustomerID'].mean(), inplace=True)
df['SalesPersonID'].fillna(df['SalesPersonID'].median(), inplace=True)
df['Discount'].fillna(0, inplace=True)

# Step 2: Fix Inconsistent Data
# Standardize categorical data entries
df['PaymentMethod'] = df['PaymentMethod'].replace({'Cheque': 'Cash'})
df['Warranty'] = df['Warranty'].replace({'Maybe': 'No'})
df['ReturnStatus'] = df['ReturnStatus'].replace({'Returned Twice': 'Returned'})

# Step 3: Remove Outliers
# Remove outliers based on Z-score for 'FinalPrice'
z_scores = np.abs(stats.zscore(df['FinalPrice']))
df = df[z_scores < 3]

# Step 4: Standardize Data Formats
# Convert date columns to datetime
df['DateOfSale'] = pd.to_datetime(df['DateOfSale'])

# Convert categorical columns to 'category' dtype
df['StoreID'] = df['StoreID'].astype('category')
df['ProductID'] = df['ProductID'].astype('category')
df['PaymentMethod'] = df['PaymentMethod'].astype('category')
df['Warranty'] = df['Warranty'].astype('category')
df['ReturnStatus'] = df['ReturnStatus'].astype('category')

# Step 5: Verify and Save the Cleaned Data
# Check the cleaned dataset
print(df.info())
print(df.head())

# Save the cleaned dataset
cleaned_file_path = '/content/mobile_sales_data.csv'
df.to_csv(cleaned_file_path, index=False)


OUTPUT:

RangeIndex: 100 entries, 0 to 99
Data columns (total 15 columns):
 #   Column                Non-Null Count  Dtype         
---  ------                --------------  -----         
 0   TransactionID         100 non-null    int64         
 1   StoreID               100 non-null    category      
 2   ProductID             100 non-null    category      
 3   CustomerID            100 non-null    float64       
 4   SalesPersonID         100 non-null    float64       
 5   DateOfSale            100 non-null    datetime64[ns]
 6   QuantitySold          100 non-null    int64         
 7   UnitPrice             100 non-null    float64       
 8   TotalSale             100 non-null    float64       
 9   Discount              100 non-null    float64       
 10  FinalPrice            100 non-null    float64       
 11  PaymentMethod         100 non-null    category      
 12  Warranty              100 non-null    category      
 13  CustomerSatisfaction  100 non-null    int64         
 14  ReturnStatus          100 non-null    category      
dtypes: category(5), datetime64[ns](1), float64(6), int64(3)
memory usage: 9.2 KB
None
   TransactionID StoreID ProductID  CustomerID  SalesPersonID DateOfSale  \
0           1001      C3       M03      1574.0           11.0 2023-09-21   
1           1002      D4       M02      1863.0           14.0 2023-10-10   
2           1003      A1       M02      1742.0           13.5 2023-01-27   
3           1004      C3       M04      1240.0           15.0 2023-08-14   
4           1005      C3       M02      1563.0           16.0 2023-10-04   

   QuantitySold  UnitPrice  TotalSale  Discount  FinalPrice   PaymentMethod  \
0             5     434.82    2174.10      5.55     2168.55            Cash   
1             7     798.77    5591.39      3.76     5587.63  Mobile Payment   
2             4     406.72    1626.88      9.27     1617.61  Mobile Payment   
3             6     937.68    5626.08      0.00     5619.01  Mobile Payment   
4             4     872.57    3490.28     11.67     3478.61            Cash   

  Warranty  CustomerSatisfaction  ReturnStatus  
0       No                     2      Returned  
1      Yes                     4  Not Returned  
2       No                     2  Not Returned  
3      Yes                     5  Not Returned  
4      Yes                     2  Not Returned  
