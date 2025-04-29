import numpy as np
import pandas as pd

size = 15
ratings = pd.DataFrame({
    "product_id": np.random.randint(100, 110, size=size),
    "user_id": np.random.randint(200, 210, size=size),
    "rating": np.random.choice([1, 2, 3, 4, 5], size=size),
    "review": np.random.choice(["Good", "Average", "Excellent", "Poor", "Fair"], size=size)
})
ratings

avg_rating = ratings.groupby("product_id")["rating"].mean()
print(avg_rating)

best_product = avg_rating.idxmax()
worst_product = avg_rating.idxmin()
best_rating = avg_rating.max()
worst_rating = avg_rating.min()

print(f"Найкращий товар: {best_product} (середній рейтинг {best_rating:.2f})")
print(f"Найгірший товар: {worst_product} (середній рейтинг {worst_rating:.2f})")

avg_rating_2 = ratings.groupby("review")["rating"].mean()
print(avg_rating_2)