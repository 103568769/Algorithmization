import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import yfinance as yf
from sklearn.linear_model import LinearRegression

sb.set()

google = yf.Ticker("GOOG").history(period='1y')["Close"]
spy = yf.Ticker("SPY").history(period='1y')["Close"]

prices = pd.DataFrame({
    "GOOG": google,
    "SPY": spy
}).dropna()

log_returns = np.log(prices / prices.shift(1)).dropna()

plt.figure(figsize=(14, 6))
log_returns.plot(title="Логарифмічна прибутковість GOOG та SPY", figsize=(14, 6))
plt.xlabel("Дата")
plt.ylabel("Лог-прибутковість")
plt.grid(True)
plt.show()

sample = log_returns.sample(n=60, random_state=42)

correlation = sample.corr().iloc[0, 1]
print(f"Коефіцієнт кореляції між GOOG та SPY: {correlation:.4f}")

plt.figure(figsize=(8, 6))
sb.scatterplot(data=sample, x="SPY", y="GOOG")
plt.title("Точкова діаграма: Лог-прибутковість GOOG vs SPY (60 точок)")
plt.xlabel("SPY лог-прибутковість")
plt.ylabel("GOOG лог-прибутковість")
plt.grid(True)
plt.show()

X = sample["SPY"].values.reshape(-1, 1)
y = sample["GOOG"].values

model = LinearRegression()
model.fit(X, y)
regression_line = model.predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Вибіркові дані")
plt.plot(X, regression_line, color="red", label="Лінія регресії")
plt.title("Лінійна регресія: GOOG ~ SPY")
plt.xlabel("SPY лог-прибутковість")
plt.ylabel("GOOG лог-прибутковість")
plt.legend()
plt.grid(True)
plt.show()

print(f"Коефіцієнт нахилу (β): {model.coef_[0]:.4f}")
print(f"Перетин з віссю (α): {model.intercept_:.4f}")
