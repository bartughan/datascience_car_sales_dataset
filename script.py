import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("car_sales.csv")  
print(data.info())
print(data.head())
# Identify missing values
print(data.isnull().sum())

# Optionally: Quick summary statistics
print(data.describe())

print("######################################")

# Clearing and standardising the data
data['price'].fillna(data['price'].mean(), inplace=True)
data['annual_income'].fillna(data['annual_income'].mean(), inplace=True)
data['company'].fillna('unknown', inplace=True)
data['car_id'] = data['car_id'].str.strip().str.lower()
data['date'] = pd.to_datetime(data['date'])
data['customer_name'] = data['customer_name'].str.strip().str.lower()
data['gender'] = data['gender'].str.strip().str.lower()
data['annual_income'] = data['annual_income'].str.strip().str.lower()
data['dealer_name'] = data['dealer_name'].str.strip().str.lower()
data['company'] = data['company'].str.strip().str.lower()
data['model'] = data['model'].str.strip().str.lower()
data['engine'] = data['engine'].str.strip().str.lower()
data['transmission'] = data['transmission'].str.strip().str.lower()
data['color'] = data['color'].str.strip().str.lower()
data['engine'] = data['engine'].str.strip().str.lower()
data['body_style'] = data['body_style'].str.strip().str.lower()
data['price'] = pd.to_numeric(data['price'], errors='coerce') 
data = data.drop_duplicates()

sns.boxplot(data['price'])
plt.show()