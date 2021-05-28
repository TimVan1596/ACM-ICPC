import numpy as np
import math

# # a=3*1的列矩阵
# a = np.random.randn(4, 3)
# # b=1*3的行矩阵
# b = np.random.randn(3, 2)
# print(a.shape)
# print(b.shape)
# print("np.dot(a, b)=")
# print(np.dot(a, b))
# aMatrix = np.mat(a)
# bMatrix = np.mat(b)
# print("矩阵相乘=")
# print(aMatrix * bMatrix)

oneA = (1 / (1 + math.exp(-9))) - 1
oneB = (2 / (1 + math.exp(-12)))

dw1 = [[
    0.5*(oneA + oneB)
], [ 0.5*(3 * oneA + 2 * oneB)]]
print(dw1)
