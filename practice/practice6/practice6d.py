import pandas as pd

orders = pd.DataFrame({
    "order_id": range(201, 211),
    "category": ["Food", "Clothes", "Food", "Tech", "Clothes", "Tech", "Food", "Clothes", "Tech", "Food"],
    "amount": [150.0, 300.0, 200.0, 800.0, 100.0, 1200.0, 250.0, 350.0, 900.0, 180.0],
    "date": pd.to_datetime(["2024-03-10", "2024-03-11", "2024-03-12", "2024-03-13", "2024-03-14",
                            "2024-03-15", "2024-03-16", "2024-03-17", "2024-03-18", "2024-03-19"])
})
orders

category_total = orders.groupby("category")["amount"].sum()
print(category_total)

top_day = orders.groupby("date")["amount"].sum().idxmax()
top_day_total = orders.groupby("date")["amount"].sum().max()
print(f"Найбільший оборот був {top_day.date()} — ${top_day_total:.2f}")

category_avg = orders.groupby("category")["amount"].mean()
print(category_avg)



