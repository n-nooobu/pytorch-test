import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#device = torch.device("cpu")
A = torch.randn(3, 5)
A = A.to(device)

print(A.get_device())
