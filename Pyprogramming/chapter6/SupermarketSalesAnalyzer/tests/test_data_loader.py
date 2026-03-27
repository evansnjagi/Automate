# imports
from modules.data_loader import read_sales_file

# Filepath
filepath = "data/sales.txt"

# Read data 
sales = read_sales_file(filepath)

# Print all sales record
for record in sales:
    print(record)