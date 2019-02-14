# monthly_sales.py

import os
import operator
import csv
import pandas as pd
import matplotlib.pyplot as plt

#
# INFO INPUTS
# OPTION C: use the os module to detect the names of all CSV files which exist in the "data" directory, then display this list to the user and prompt the user to input their selection.
#

# ... USD adapted from https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(any_price):
    return "${0:,.2f}".format(any_price)

# adapted from: https://docs.python.org/2.7/library/os.path.html#os.path.isdir
path = os.path.join("data")
directory = os.listdir(path)

print("-----------------------")
print("THE FOLLOWING ARE THE MONTHLY SALES DATA FILES: ")
print (" ") #for formatting

x = 1
for d in directory:
    print("  " + str(x) + ") " + d)
    x = x + 1

print (" ") #for formatting

# with help from https://georgetown-opim-py.slack.com/messages/DFA4T5HGB/ (@sarahmandi)
chosen_file = []
while True:
    user_input = input("PLEASE CHOOSE A FILE NAME TO ANALYZE as 'sales-YYYYMM.csv' : ")
    if user_input in directory:
        chosen_file.append(user_input)
        break
    else:
        print("Oops! Filename not found, please try again.")
        continue

#csv_filename = "sales-201802.csv"
csv_filename = user_input
csv_filepath = os.path.join("data", csv_filename)
csv_data = pd.read_csv(csv_filepath) #> read CSV into pandas dataframe object[df object is now "csv_data"]


#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum() #> from the dataframe we just made, sum the sales prices to get the monthly total
#print(type(monthly_total), monthly_total)

# Find unique products

# ... adapted from https://github.com/s2t2/exec-dash-starter-py/commit/f790f124895db77920e37655c91e1e5a7a424aaa
product_names = csv_data["product"] #> from dataframe, list only the product name
#print(type(product_names), product_names) > this is 'pandas.core.series.Series'
unique_product_names = product_names.unique()
#print(type(unique_product_names), unique_product_names) > this is  'numpy.ndarray' > google how to convert to a list
unique_product_names = unique_product_names.tolist() # convert numpy.ndarray to list

# Now that we have unique products, find total sales per unique product

top_sellers = [] #> empty list so that we can customize

#... adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_solution_further_alt.py
for product_name in unique_product_names:
    #define matching_rows as any duplicate
    matching_rows = csv_data[csv_data["product"] == product_name]
    #print(type(matching_rows))
    #> this is a 'pandas.core.frame.DataFrame'>
    product_monthly_sales = matching_rows["sales price"].sum()
    #now adding in product name and monthly sales
    top_sellers.append(
        {"name": product_name, "monthly_sales": product_monthly_sales})
    #print(top_sellers)
    #print(type(top_sellers)) > it is a list!
    #> this gives us each unique product and their monthly sales

# Now that we have monthly sales for each unique product, we need to sort in descending order our list

#... adapted from https://docs.python.org/3/howto/sorting.html
top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)
#print(top_sellers) this gives us the right info but not formatted correctly

#
# OUTPUTS
#

#  dates adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py
def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

month = month_lookup(csv_filename[-6:-4]) #use this to change specific elements of the filename chosen by user
year = int(csv_filename[6:10]) 

print("-----------------------")
print(("MONTH: ") + str(month) + (" ")+ str(year))

print("-----------------------")
print("CRUNCHING THE DATA...")


#monthly_total_usd = "${0:.2f}".format(monthly_total)
#print("Subtotal: " + str(monthly_total_usd)) 
# > this way is more complicated than making a user-defined function so don't use.

print("-----------------------")
#...  from https://github.com/s2t2/exec-dash-starter-py/commit/1bf69cc8c8c4d26d8aa265b4fc984cd01ad894ff
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")


print("-----------------------")
print("TOP SELLING PRODUCTS:")

#...  from https://github.com/s2t2/exec-dash-starter-py/commit/1bf69cc8c8c4d26d8aa265b4fc984cd01ad894ff
rank = 1 #we are defining a variable here to use in our list printing
for d in top_sellers:
    #breakpoint()
    print("  " + str(rank) + ") " + d["name"] + ": " +  to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")

#...adapted from https://github.com/carolinefeeney/sales-reporting/commit/fae68cf4805345d23ae1f884501e021fa01ae2a3
chart_title = ("Top Selling Products (")+ str(month) + (" ") + str(year) + (")")

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")
plt.show()