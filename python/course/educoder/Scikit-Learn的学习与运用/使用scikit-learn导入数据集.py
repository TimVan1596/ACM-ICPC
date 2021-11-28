from sklearn import datasets

# 加载并返回波士顿房价数据集（回归）
datasets.load_boston([return_X_y])
# 加载并返回iris数据集（分类）
datasets.load_iris([return_X_y])
# 加载并返回糖尿病数据集（回归）
datasets.load_diabetes([return_X_y])
# 加载并返回数字数据集（分类）
datasets.load_digits([n_class, return_X_y])
# 加载并返回linnerud数据集（多分类）
datasets.load_linnerud([return_X_y])
