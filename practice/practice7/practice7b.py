import torch

tensor1 = torch.randn(5, 5)
tensor2 = torch.randn(5, 5)

print("Тензор 1:")
print(tensor1)
print("\nТензор 2:")
print(tensor2)

mask = tensor1 > tensor2
print("\nМаска:")
print(mask)

masked_tensor = tensor1 * mask.float()
print("\nТензор після маскування:")
print(masked_tensor)


