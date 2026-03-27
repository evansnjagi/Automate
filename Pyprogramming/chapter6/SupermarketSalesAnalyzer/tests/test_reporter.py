# Import modules
from modules.data_loader import read_sales_file
from modules.processor import SalesProcessor
from modules.reporter import write_summary

# file paths
sales_path = "data/sales.txt"
summary_path = "data/summary.txt"

# Read data
data = read_sales_file(sales_path)

# Process the data
sp = SalesProcessor(data)
product_total = sp.total_sales_per_product()
daily_total = sp.total_sales_per_day()

# Reporting
write_summary(summary_path, product_total, daily_total)
print("Report generated successfully!")