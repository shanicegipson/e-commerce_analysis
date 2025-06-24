import pandas as pd
import test

file_path = '../data/raw/data.csv'

try:
    sales_df = pd.read_csv(file_path)
except UnicodeDecodeError:
    sales_df = pd.read_csv(file_path, encoding="latin-1")  # Or another encoding like "ISO-8859-1"



print(sales_df.dtypes)

####### Calculates the total sales - COMPLETED!
# quantity = sales_df['Quantity']
# unit_price = sales_df['UnitPrice']
# total_sales = quantity * unit_price
# print(total_sales.sum())


####### Grabs the top 5/ 10 items sold - COMPLETED!
top_five_products = sales_df['StockCode'].str.upper().value_counts()[:5]
top_ten_products = sales_df['StockCode'].str.upper().value_counts()[:10]

desctiption = sales_df['Description'].value_counts()
print("================")
print(stock_code)
# print(desctiption)


print("================")
# top_sale = sales_df['StockCode'].value_counts()['85123a']
# print(f"Top item: {top_sale}")
# for index, row in sales_data.iterrows():
#     rows_value = row.to_dict()
#     counts = {}
#     times_run = 0
#
#     if times_run < 3:
#         for product_code in product_codes:
#             counts[product_code] = (row == product_code).sum()
#     print(f"Row {index}: {counts}")
#     break

