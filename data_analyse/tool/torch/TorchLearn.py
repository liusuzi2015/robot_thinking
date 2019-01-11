
import numpy as np
import torch

# 创建一个张量
x = torch.Tensor(3, 4)
print("Type: {}".format(x.type()))
print("Size: {}".format(x.shape))
print("Values: \n{}".format(x))

# 创建一个随机张量
x = torch.randn(2, 3) # torch.randn对应于正态分布，而rand(2,3)对应于均匀分布
print (x)

# 0和1张量
x = torch.zeros(2, 3)
print (x)
x = torch.ones(2, 3)
print (x)

# 列表（List） → 张量
x = torch.Tensor([[1, 2, 3],[4, 5, 6]])
print("Size: {}".format(x.shape))
print("Values: \n{}".format(x))

# NumPy 数组 → 张量
x = torch.from_numpy(np.random.rand(2, 3))
print("Size: {}".format(x.shape))
print("Values: \n{}".format(x))

# 改变张量类型（张量默认为float类型）
x = torch.Tensor(3, 4)
print("Type: {}".format(x.type()))
x = x.long()
print("Type: {}".format(x.type()))

# CUDA可用吗？
print (torch.cuda.is_available())