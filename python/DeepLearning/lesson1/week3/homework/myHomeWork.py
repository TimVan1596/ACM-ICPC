import numpy as np
import matplotlib.pyplot as plt
from testCases import *
import sklearn
import sklearn.datasets
import sklearn.linear_model
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets

np.random.seed(1)
X, Y = load_planar_dataset()
# plt.scatter(X[0, :], X[1, :], c=np.squeeze(Y), s=40, cmap=plt.cm.Spectral)
# plt.plot(X[0, :], X[1, :], marker='o',linestyle='None')
print(X.shape)
print(Y.shape)
# print(Y)
# plt.show()
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X.T, Y.T)

plot_decision_boundary(lambda x: clf.predict(x), X, Y)  # 绘制决策边界
plt.title("Logistic Regression")  # 图标题
LR_predictions = clf.predict(X.T)  # 预测结果
print("逻辑回归的准确性： %d " % float((np.dot(Y, LR_predictions) +
                               np.dot(1 - Y, 1 - LR_predictions)) / float(Y.size) * 100) +
      "% " + "(正确标记的数据点所占的百分比)")
plt.show()
