def write_summary(filepath, product_total, daily_total):
    """
    Write sales summary to a file.

    Parameters:
    filepath(str): Output file path
    product_total(dict): Sales per product
    daily_total(dict): Sales per day
    """
    with open(filepath, "w") as file:
        file.write("=== Sales Summary Report ===\n\n")

        file.write("Sales per product: \n")
        file.write("-"* 25 + "\n")

        for product, sales in sorted(product_total.items(), key = lambda x: x[1], reverse =True):
            file.write(f"{product:<10}: KES {sales:,.2f}\n")
        
        # Daily sales
        file.write("\nSales per day:\n")
        file.write("-"* 25 + "\n")

        for day, sales in sorted(daily_total.items(), key = lambda x: x[1], reverse=True):
            file.write(f"{day}: KES {sales:,.2f}\n")