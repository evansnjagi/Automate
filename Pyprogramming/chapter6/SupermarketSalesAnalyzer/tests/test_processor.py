# Import modules
from modules.data_loader import read_sales_file
from modules.processor import SalesProcessor

# Filepath
filepath  = "data/sales.txt"

# Read data
data = read_sales_file(filepath)

# Get totals
sp = SalesProcessor(data)

product_totals = sp.total_sales_per_product()
daily_totals = sp.total_sales_per_day()

print(f"Sale per product: {product_totals}")
print(f"Daily sales: {daily_totals}")

