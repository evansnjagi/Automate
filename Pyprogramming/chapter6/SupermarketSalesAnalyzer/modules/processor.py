class SalesProcessor:
    def __init__(self, sales_data):
        self.data = sales_data

    def total_sales_per_product(self):
        """"
        Calculate total revenue per product
        """
        data = self.data
        product_sales = {}

        for record in self.data:
            product = record["product"]
            revenue = record["quantity"] * record["price"]

            # Aggregation
            if product in product_sales:
                product_sales[product] += revenue
            else:
                product_sales[product] = revenue
        return product_sales
    
    def total_sales_per_day(self):
        """
        Calculate total revenue per day
        """
        daily_sales = {}

        for record in self.data:
            date = record["date"]
            revenue = record["quantity"] * record["price"]

            # Aggregation
            if date in daily_sales:
                daily_sales[date] += revenue
            else:
                daily_sales[date] = revenue

        return daily_sales
                
