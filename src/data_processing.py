import pandas as pd
import test

file_path = '../data/raw/data.csv'

try:
    sales_data = pd.read_csv(file_path)
except UnicodeDecodeError:
    sales_data = pd.read_csv(file_path, encoding="latin-1")  # Or another encoding like "ISO-8859-1"



print(sales_data.isnull().sum())

####### Calculates the total sales - COMPLETED!
#quantity = sales_data['Quantity']
#unit_price = sales_data['UnitPrice']
#total_sales = quantity * unit_price
#print(total_sales.sum())

