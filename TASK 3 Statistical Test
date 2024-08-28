import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = '/content/mobile_sales_data.csv'
df = pd.read_csv(file_path)

# Ensure relevant columns are numeric
df['QuantitySold'] = pd.to_numeric(df['QuantitySold'], errors='coerce')
df['FinalPrice'] = pd.to_numeric(df['FinalPrice'], errors='coerce')

# Handle missing values
df.dropna(inplace=True)

# Label encode categorical variables if needed
encoder = LabelEncoder()
df['StoreID'] = encoder.fit_transform(df['StoreID'])
df['PaymentMethod'] = encoder.fit_transform(df['PaymentMethod'])

# Statistical Tests

# 1. T-Test (Independent Samples)
def independent_t_test(df, group_col, value_col, group1, group2):
    group1_data = df[df[group_col] == group1][value_col]
    group2_data = df[df[group_col] == group2][value_col]
    t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
    return t_stat, p_value

# 2. Paired T-Test
def paired_t_test(before_data, after_data):
    t_stat, p_value = stats.ttest_rel(before_data, after_data)
    return t_stat, p_value

# 3. Chi-Square Test
def chi_square_test(df, col1, col2):
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2_stat, p_value

# 4. ANOVA (One-Way)
def anova_test(df, group_col, value_col):
    groups = df[group_col].unique()
    group_data = [df[df[group_col] == group][value_col] for group in groups]
    f_stat, p_value = stats.f_oneway(*group_data)
    return f_stat, p_value

# 5. Pearson Correlation
def pearson_correlation(df, col1, col2):
    correlation, p_value = stats.pearsonr(df[col1], df[col2])
    return correlation, p_value

# 6. Spearman Correlation
def spearman_correlation(df, col1, col2):
    correlation, p_value = stats.spearmanr(df[col1], df[col2])
    return correlation, p_value

# Example usage:
# T-Test between two stores on FinalPrice
t_stat, p_value = independent_t_test(df, 'StoreID', 'FinalPrice', 0, 1)
print(f"T-Test: t-statistic = {t_stat}, p-value = {p_value}")

# Paired T-Test on FinalPrice before and after a discount
before_discount = df['FinalPrice']
after_discount = df['FinalPrice'] * 0.9  # Assume a 10% discount
t_stat, p_value = paired_t_test(before_discount, after_discount)
print(f"Paired T-Test: t-statistic = {t_stat}, p-value = {p_value}")

# Chi-Square Test between StoreID and ReturnStatus
chi2_stat, p_value = chi_square_test(df, 'StoreID', 'ReturnStatus')
print(f"Chi-Square Test: chi2_stat = {chi2_stat}, p-value = {p_value}")

# ANOVA on FinalPrice across different stores
f_stat, p_value = anova_test(df, 'StoreID', 'FinalPrice')
print(f"ANOVA: F-statistic = {f_stat}, p-value = {p_value}")

# Pearson Correlation between QuantitySold and FinalPrice
correlation, p_value = pearson_correlation(df, 'QuantitySold', 'FinalPrice')
print(f"Pearson Correlation: correlation = {correlation}, p-value = {p_value}")

# Spearman Correlation between QuantitySold and FinalPrice
correlation, p_value = spearman_correlation(df, 'QuantitySold', 'FinalPrice')
print(f"Spearman Correlation: correlation = {correlation}, p-value = {p_value}")

OUTPUT:

T-Test: t-statistic = 1.0280246241657476, p-value = 0.309556665931133
Paired T-Test: t-statistic = 13.155216308292434, p-value = 1.848823529093599e-23
Chi-Square Test: chi2_stat = 6.535071499013806, p-value = 0.08828958495547007
ANOVA: F-statistic = 1.6614584598472635, p-value = 0.18046155336215675
Pearson Correlation: correlation = 0.6813817064507969, p-value = 6.093484875287343e-15
Spearman Correlation: correlation = 0.7079585826202686, p-value = 1.7748308002916958e-16
