import numpy as np

# Create a 3D NumPy array for sales data (e.g., [Product, Region, Quarter])
sales_data = np.array([
    [[100, 150], [200, 250]],  # Product A, Region 1, Q1 and Q2
    [[300, 350], [400, 450]]   # Product B, Region 1, Q1 and Q2
])

# Display sales data
print("Sales Data (Product x Region x Quarter):")
print(sales_data)

# Example of aggregating data (total sales for Product A across regions and quarters)
total_sales_product_a = np.sum(sales_data[0, :, :])
print(f"Total Sales for Product A: {total_sales_product_a}")
