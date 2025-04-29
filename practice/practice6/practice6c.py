import pandas as pd

employees = pd.DataFrame({
    "id": range(1, 11),
    "name": ["Ivan", "Oksana", "Petro", "Olena", "Dmytro", "Nina", "Serhii", "Oleg", "Anna", "Viktoria"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "salary": [5000.0, None, 6000.0, 7000.0, None, 6500.0, 7200.0, 4800.0, None, 5500.0],
    "experience": [5, 3, None, 10, 2, 8, 6, None, 4, 7]
})
employees

employees["salary"] = employees.groupby("department")["salary"].transform(
    lambda x: x.fillna(x.mean())
)

employees["experience"] = employees["experience"].fillna(employees["experience"].median())

avg_salary = employees.groupby("department")["salary"].mean()
top_department = avg_salary.idxmax()
top_salary = avg_salary.max()

print(f"Відділ з найвищою середньою зарплатою: {top_department} (${top_salary:.2f})")