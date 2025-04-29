import pandas as pd

data = pd.DataFrame({
    "ПІБ": ["Іваненко І.П.", "Петренко О.О.", "Сидоренко А.А.", "Мельник Ю.Ю.", "Ковальчук Н.Н."],
    "Зріст": [175, 168, 182, 170, 178],
    "Вага": [72, 65, 80, 68, 75]
}, index=["А", "Б", "В", "Г", "Д"])

print("Початковий датафрейм:")
print(data)

height_sort = data.sort_values(by="Зріст")
print("\nВідсортовано за зростанням зрісту:")
print(height_sort)

weight_sort = data.sort_values(by="Вага", ascending=False)
print("\nВідсортовано за спаданням ваги:")
print(weight_sort)

