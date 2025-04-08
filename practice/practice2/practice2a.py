import random

numbers = [random.randint(1, 100) for _ in range(10)]
odd = [num for num in numbers if num % 2 != 0]
print (numbers)

if odd:
    max_odd = max(odd)
    min_odd = min(odd)
    max_count = str(numbers.count(max_odd))
    min_count = str(numbers.count(min_odd))
    max_odd2 = str(max_odd)
    min_odd2 = str(min_odd)
    print("Найбільше непарне число: " + max_odd2 + ". У масиві їх " + max_count)
    print("Найменше непарне число: " + min_odd2 + ". У масиві їх " + min_count)
else:
    print("Парних чисел немає")

n = int(input("Введіть початок проміжку: "))
m = int(input("Введіть кінець проміжку: "))

even = [num for num in numbers if num % 2 == 0 and n <= num <= m]
sum_even = str(sum(even))
print ("Сума парних чисел у вказаному проміжку: " + sum_even)