import torch
x = torch.tensor([1,2])
print(x)
x = x.new_ones(5,3)
print(x)