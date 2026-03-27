def read_sales_file(filepath):
    """
    Reads sales data from the txt file.

    Parameters:
    filepath(str): Path to the text.txt file.

    Returns:
    List of dict: Each dict represents a sales record.
    """
    # Instantiate sales data
    sales_data = []

    # Open and read the file
    with open(filepath, "r") as f:
        lines = f.readlines()

        # Skip header row
        for line in lines[1:]:
            date, product, quantity, price = line.strip().split(",")

            # Appending to the list
            sales_data.append(
                {
                    "date": date,
                    "product": product,
                    "quantity": int(quantity),
                    "price": float(price)
                }
            )

    return sales_data