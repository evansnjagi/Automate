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

        for product, sales in product_total.items():
            file.write(f"{product}: {sales}\n")
        
        # Daily sales
        file.write("\nSales per day:\n")

        for day, sales in daily_total.items():
            file.write(f"{day}: {sales}\n")