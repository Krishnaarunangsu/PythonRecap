# Read csv file
import pandas as pd

# path of the CSV file
# csv_path = "..\\..\\..\\data\\csv\\Salaries.csv"
csv_path = "https://raw.githubusercontent.com/Padre-Media/dataset/main/Ames.csv"

# Load the csv file and create the dataframe
# df_csv = pd.read_csv(csv_path)
df_csv = pd.read_csv(filepath_or_buffer=csv_path)
# print(f'Salaries CSV to pandas Dataframe:\n{df_csv}')
# print(df_csv.dtypes)
print(df_csv.columns)

# Descriptive Statistics of Sales Price
sales_price_description = df_csv['SalePrice'].describe()
print(f'Sales Price Description:\n{sales_price_description}')

median_sale_price=df_csv['SalePrice'].median()
print(f'Median of Sales Price Description:{median_sale_price}')

mode_sale_price=df_csv['SalePrice'].mode()
print(f'Mode of Sales Price Description:{mode_sale_price}')
mode_sale_price_index=df_csv['SalePrice'].mode().values[0]
print(f'Mode of Sales Price Description:{mode_sale_price_index}')

range_sale_price = df_csv['SalePrice'].max() - df_csv['SalePrice'].min()
print(f"Range of Sale Price:{range_sale_price}")

variance_sale_price = df_csv['SalePrice'].var()
print(f"Variance of Sale Price:{variance_sale_price}")

std_dev_sale_price = df_csv['SalePrice'].std()
print(f"Standard Deviation of Sale Price:{std_dev_sale_price}")

# https://machinelearningmastery.com/decoding-data-descriptive-statistics/

skewness_sale_price = df_csv['SalePrice'].skew()
print(f"Skewness of Sale Price:{skewness_sale_price}")

kurtosis_sale_price = df_csv['SalePrice'].kurt()
print(f"Kurtosis of Sale Price:{kurtosis_sale_price}")

tenth_percentile = df_csv['SalePrice'].quantile(0.10)
ninetieth_percentile = df_csv['SalePrice'].quantile(0.90)
print(f"10th Percentile:{tenth_percentile}")
print(f"90th Percentile:{ninetieth_percentile}")

q1_sale_price = df_csv['SalePrice'].quantile(0.25)
q2_sale_price = df_csv['SalePrice'].quantile(0.50)
q3_sale_price = df_csv['SalePrice'].quantile(0.75)
print(f"Q1 (25th Percentile):{q1_sale_price}")
print(f"Q2 (Median/50th Percentile):{q2_sale_price}")
print(f"Q3 (75th Percentile):{q3_sale_price}")

iqr_sale_price = df_csv['SalePrice'].quantile(0.75) - df_csv['SalePrice'].quantile(0.25)
print(f"IQR of Sale Price:{iqr_sale_price}")

