import numpy as np

# a=3*1的列矩阵
a = np.random.randn(4, 3)
# b=1*3的行矩阵
b = np.random.randn(3, 2)
print(a.shape)
print(b.shape)
print("np.dot(a, b)=")
print(np.dot(a, b))
aMatrix = np.mat(a)
bMatrix = np.mat(b)
print("矩阵相乘=")
print(aMatrix * bMatrix)
