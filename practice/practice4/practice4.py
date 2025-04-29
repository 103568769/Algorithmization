import pandas as pd

temperatures = pd.Series(
    [17, 19, 21, 19, 22, 21, 18],  # значення температур (пн-нд)
    index=["Понеділок", "Вівторок", "Середа", "Четвер", "П’ятниця", "Субота", "Неділя"]
)

max_temp = temperatures.max()
min_temp = temperatures.min()

max_temp_days = temperatures[temperatures == max_temp].index.tolist()
min_temp_days = temperatures[temperatures == min_temp].index.tolist()

avg_temp = temperatures.mean()

print(f"Максимальна температура: {max_temp}°C у: {', '.join(max_temp_days)}")
print(f"Мінімальна температура: {min_temp}°C у: {', '.join(min_temp_days)}")
print(f"Середня температура тижня: {avg_temp:.2f}°C")