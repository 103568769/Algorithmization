import pandas as pd

sales = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "date": pd.to_datetime(["2024-03-10", "2024-03-11", "2024-03-12", "2024-03-13", "2024-03-14",
                            "2024-03-15", "2024-03-16", "2024-03-17", "2024-03-18", "2024-03-19"]),
    "product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet", "Laptop"],
    "quantity": [2, 5, 3, 1, 2, 3, 4, 1, 5, 2],
    "price": [1200.0, 600.0, 800.0, 1500.0, 650.0, 1400.0, 850.0, 620.0, 900.0, 1300.0],
    "customer": ["Ivanov", "Petrov", "Sidorov", "Kozlov", "Smirnov", "Fedorov", "Titov", "Orlov", "Belov", "Nikolaev"],
    "region": ["East", "West", "North", "South", "East", "North", "West", "South", "East", "West"]
})
sales

sales["total_price"] = sales["quantity"] * sales["price"]

product_revenue = sales.groupby("product")["total_price"].sum()
top_product = product_revenue.idxmax()
top_revenue = product_revenue.max()

print(f"Найбільше доходу приніс товар: {top_product} (${top_revenue:.2f})")

region_quantity = sales.groupby("region")["quantity"].sum()

print(region_quantity)