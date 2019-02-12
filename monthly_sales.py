# monthly_sales.py

import os
import operator
import csv
import pandas
import matplotlib as plt


#
# INFO INPUTS
#

#TODO format as USD

csv_filename = "sales-201710.csv" #TODO allow user to specify with FILEPATH
# ... adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)  #> reference a file in the data directory
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = csv_data = pandas.read_csv(csv_filepath) #> read CSV into pandas dataframe object[df object is now "csv_data"]

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum() #> from the dataframe we just made, sum the sales prices to get the monthly total
#print(monthly_total)

# ... adapted from https://github.com/s2t2/exec-dash-starter-py/commit/f790f124895db77920e37655c91e1e5a7a424aaa
product_names = csv_data["product"] #> from dataframe, list only the product name
#print(product_names)
#print(type(product_names))
#> this is 'pandas.core.series.Series'
unique_product_names = product_names.unique()
#print(unique_product_names)
#print(type(unique_product_names))
#> this is  'numpy.ndarray' > google how to convert to a list
unique_product_names = unique_product_names.tolist() # convert numpy.ndarray to list





print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")