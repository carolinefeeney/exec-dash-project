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
csv_data = csv_data = pandas.read_csv(csv_filepath) #> read CSV into pandas dataframe object


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