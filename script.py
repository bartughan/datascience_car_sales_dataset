import pandas as pd

data = pd.read_csv("car_sales.csv")  # Replace with your file path
print(data.info())
print(data.head())
