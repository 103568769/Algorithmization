import torch

tensor = torch.randn(10, 5)
print("Оригінальний тензор:")
print(tensor)

avg_value = tensor.mean()
print(f"\nСереднє значення тензора: {avg_value.item()}")

filtered_tensor = tensor[tensor > avg_value]
print("\nФільтрований тензор (елементи, що перевищують середнє значення):")
print(filtered_tensor)

