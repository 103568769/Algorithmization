import numpy as np

array = np.random.randint(3, 8, size=(3, 5))
print("Масив:\n", array)

odd_counts = np.sum(array % 2 != 0, axis=1)
max_odd = np.max(odd_counts)
rows = np.where(odd_counts == max_odd)[0]

if len(rows) == 1:
    print("Номер рядка з максимальною кількістю непарних елементів:", rows[0])
else:
    print("Номери рядків з однаковою максимальною кількістю непарних елементів:", rows)

