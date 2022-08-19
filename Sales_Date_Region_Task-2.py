# Library
from timeit import timeit

import pandas as pd

# import the csv file
sales_1 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_0.csv')
# print(sales_1.head(5))

# data types of each column
print('The data type of product is :', type(sales_1['product'][0]))
print('The data type of price is :', type(sales_1['price'][0]))
print('The data type of quantity is :', type(sales_1['quantity'][0]))
print('The data type of date is :', type(sales_1['date'][0]))
print('The data type of region is :', type(sales_1['region'][0]))

# Requirement 1
# Filter out the rows whose product value is not pink morsel.
# sales_1 = sales_1[sales_1.product == 'pink morsel']
# measure the time it takes to scan the sheet %timeit
# print("The tme taken to scan the entire sheet :", timeit, sales_1.query('product == "pink morsel"'))
sales_1 = sales_1.query('product == "pink morsel"')
# print(sales_1.head(10))

# Requirement 2
# Should get rid of the $ in the price column
# print("The time taken to strip the $ from the entire column :", timeit, [x.strip('$') for x in sales_1.price])
sales_1['price'] = [x.strip('$') for x in sales_1.price]
# sales_1['price] = [x[1:] for x in sales_1.price] if x[0] == '$' else x
# print(sales_1.head(5))

# We need to change the data type of the column price and date
sales_1['price'] = pd.to_numeric(sales_1['price'])
sales_1['date'] = pd.to_datetime(sales_1['date'])
print(sales_1.dtypes)

# new sale column = price * quantity
sales_1['Sales'] = sales_1['price'] * sales_1['quantity']
# print(sales_1.head(5))

# drop the columns price, quantity, product.
sales_1 = sales_1.drop(sales_1.columns[[0, 1, 2]], axis=1)
# change the column names
sales_1 = sales_1.rename(columns={'date': 'Date', 'region': 'Region'})
# Rearrange
cols = sales_1.columns.tolist()
cols = cols[-1:] + cols[:-1]
sales_1 = sales_1[cols]
print(sales_1.head(5))

# sales_2, sales_3
sales_2 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_1.csv')
sales_3 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_2.csv')

# Filter product col
sales_2 = sales_2.query('product == "pink morsel"')
sales_3 = sales_3.query('product == "pink morsel"')

# Strip the $ from the price column
sales_2['price'] = [x.strip('$') for x in sales_2.price]
sales_3['price'] = [x.strip('$') for x in sales_3.price]

# Convert the data type of price and date
sales_2['price'] = pd.to_numeric(sales_2['price'])
sales_3['price'] = pd.to_numeric(sales_3['price'])
sales_2['date'] = pd.to_datetime(sales_2['date'])
sales_3['date'] = pd.to_datetime(sales_3['date'])

# Product of price and quantity
sales_2['Sales'] = sales_2['price'] * sales_2['quantity']
sales_3['Sales'] = sales_3['price'] * sales_3['quantity']

# drop the cols
sales_2 = sales_2.drop(sales_2.columns[[0, 1, 2]], axis=1)
sales_3 = sales_3.drop(sales_3.columns[[0, 1, 2]], axis=1)

# Change cols names
sales_2 = sales_2.rename(columns=({'date': 'Date', 'region': 'Region'}))
sales_3 = sales_3.rename(columns=({'date': 'Date', 'region': 'Region'}))

# Rearrange
cols = sales_2.columns.tolist()
cols = cols[-1:] + cols[:-1]
sales_2 = sales_2[cols]
sales_3 = sales_3[cols]

# Print
print(sales_2.head(5))
print(sales_3.head(5))

# Combine all the sales
sales_dataframes = [sales_1, sales_2, sales_3]
print('The count of sales_1 : {0}, sales_2: {1}, sales_3 : {2}'.format(sales_1.size, sales_2.size, sales_3.size))
print('The total count  of all the sales is ', sales_1.size + sales_2.size + sales_3.size)
sales_2018_2022 = pd.concat(sales_dataframes)
print('The total count of sales_2018_2022 :', sales_2018_2022.size)
print(sales_2018_2022.head(5))

# Writing to the csv file
sales_2018_2022.to_csv('Daily_sales_2018_2020.csv', index=False)

