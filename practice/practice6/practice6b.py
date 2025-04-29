import pandas as pd

customers = pd.DataFrame({
    "customer_id": range(1, 11),
    "name": ["Anna", "Oleg", "Maria", "Ivan", "Olena", "Petro", "Dmytro", "Nina", "Serhii", "Viktoria"],
    "age": [25, 40, 35, 50, 28, 33, 38, 45, 30, 42],
    "city": ["Kyiv", "Lviv", "Odesa", "Dnipro", "Kharkiv", "Lviv", "Kyiv", "Odesa", "Kharkiv", "Dnipro"],
    "purchases": [5, 2, 7, 3, 4, 6, 1, 8, 5, 3]
})
customers

average_age = customers["age"].mean()
print(f"Середній вік клієнтів: {average_age:.1f} років")

city_counts = customers["city"].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()
print(f"Найбільше клієнтів у місті: {top_city} ({top_city_count} клієнтів)")

active_customers = customers[customers["purchases"] > 3]
print(active_customers)

