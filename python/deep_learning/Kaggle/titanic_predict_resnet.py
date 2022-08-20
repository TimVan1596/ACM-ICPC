import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.keras import activations
import matplotlib.pyplot as plt
from tensorflow.keras import layers, Sequential, Model
import datetime

# 显示训练情况


def plot_history(history):
    # histoty的返回值
    # 一个历史对象。它的 History.history 属性是连续 epoch 的训练损失值和指标值的记录，以及验证损失值和验证指标值（如果适用）。
    # history.history：loss、accuracy、val loss、val accuracy
    hist = pd.DataFrame(history.history)
    hist["epoch"] = history.epoch

    plt.figure()
    plt.xlabel("Num of Epochs")
    plt.ylabel("value")
    plt.plot(hist["epoch"], hist["accuracy"], label="accuracy")
    plt.plot(hist["epoch"], hist["val_accuracy"], label="val_accuracy")
    plt.ylim([0, 1])
    plt.legend()
    plt.show()


# 导入数据
def load_data(path_url, test_path_url):
    raw_train_dataset = pd.read_csv(path_url)
    raw_test_dataset = pd.read_csv(test_path_url)
    return raw_train_dataset, raw_test_dataset


# 数据预处理的基础方法
def preprocess(raw_dataset, features, train=True):
    """用于predict的数据预处理
    Args:
        input: dataset = pandas.DataFrame对象
    """
    # 以中位数来替代
    if "Age" in features:
        raw_dataset["Age"].fillna(raw_dataset["Age"].median(), inplace=True)
    raw_dataset["Fare"].fillna(raw_dataset["Fare"].median(), inplace=True)
    raw_dataset["Embarked"].fillna(raw_dataset["Fare"].median(), inplace=True)
    dataset = raw_dataset[features]
    dataset = dataset.copy()

    # 由于 embarked=登船港口, Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton

    Embarked = dataset.pop("Embarked")

    # 根据 embarked 列来写入新的 3 个列
    dataset["S"] = (Embarked == "S") * 1.0
    dataset["C"] = (Embarked == "C") * 1.0
    dataset["Q"] = (Embarked == "Q") * 1.0

    # 根据 sex 列来写入新的 2 个列
    Sex = dataset.pop("Sex")
    dataset["Male"] = (Sex == "male") * 1.0
    dataset["Female"] = (Sex == "female") * 1.0

    dataset_withoutna = dataset
    if train:
        labels = dataset_withoutna["Survived"]
        dataset_withoutna.pop("PassengerId")
        dataset_withoutna.pop("Survived")
        # 标准化
        train_stats = dataset_withoutna.describe()
        train_stats = train_stats.transpose()
        normed_train_data = (dataset_withoutna - train_stats["mean"]) / train_stats[
            "std"
        ]
        return np.array(normed_train_data), np.array(labels)
    else:
        labels = dataset.pop("PassengerId")
        dataset.fillna(0, inplace=True)
        test_stats = dataset.describe()
        test_stats = test_stats.transpose()
        normed_test_data = (dataset - test_stats["mean"]) / test_stats["std"]
        return np.array(normed_test_data), np.array(labels)


# 训练
def train(train_dataset, labels, epochs=120, batch_size=512, is_plot=False):

    input_ = layers.Input(shape=(train_dataset.shape[1]))

    # 残差网络
    output = Sequential([layers.BatchNormalization(), layers.Dropout(0.2),
                         layers.Dense(256, activation="elu"),
                         layers.BatchNormalization(),
                         layers.Dense(128, activation="elu")])(input_)

    answer1 = Sequential([layers.BatchNormalization(),
                          layers.Dropout(0.3),
                          layers.Dense(64, "relu")])(output)

    answer2 = Sequential([layers.BatchNormalization(), layers.Dense(64, "elu"),
                          layers.BatchNormalization(),
                          layers.Dense(32, "relu")])(layers.Concatenate()([output, answer1]))

    answer4 = Sequential([layers.BatchNormalization(),
                          layers.Dense(256, kernel_initializer=tf.keras.initializers.lecun_normal(seed=42),
                                       activation='selu', name='last_frozen'), layers.BatchNormalization(),
                          layers.Dense(206, kernel_initializer=tf.keras.initializers.lecun_normal(seed=42),
                                       activation='selu')])(layers.Concatenate()([output, answer1, answer2]))

    answer5 = Sequential([layers.BatchNormalization(),
                          layers.Dense(1)])(answer4)
    model = Model(inputs=[input_, ], outputs=answer5)

    # 在 Keras 中提供了 compile()和 fit()函数方便实现逻辑。
    # compile：首先通过compile 函数指定网络使用的优化器对象、损失函数类型，评价指标等设定，这一步称为装配
    # fit： 模型装配完成后，即可通过 fit()函数送入待训练的数据集和验证用的数据集
    model.compile(
        # Adam的学习律默认为0.001
        optimizer=tf.keras.optimizers.Adam(),
        # BinaryCrossentropy:计算真实标签和预测标签之间的交叉熵损失
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        # 设置测量指标为准确率
        metrics=["accuracy"],
    )

    # 模型装配完成后，即可通过 fit()函数送入待训练的数据集和验证用的数据集，这一步称为模型训练
    # verbose = 'auto'、0、1 或 2 详细模式。
    # 0 = 静音，1 = 进度条，2 = 每个 epoch 一行。'auto' 在大多数情况下默认为 1
    history = model.fit(
        x=train_dataset,
        y=labels,
        epochs=epochs,
        validation_split=0.3,
        batch_size=batch_size,
        verbose="auto",
        # callbacks=[early_stop]
    )

    # 显示训练情况
    if is_plot:
        plot_history(history)

    # 可以通过 Model.evaluate(db)循环测试完 db 数据集上所有样本
    loss, accuracy = model.evaluate(train_dataset, labels, verbose=2)
    print("Accuracy:", accuracy)

    return model


# 真实预测并输出csv
def predict_out(model, csv_path):
    # model.evaluate 和 model.predict 的区别
    # https://blog.csdn.net/DoReAGON/article/details/88552348
    # 两者差异：
    # 1
    # 输入输出不同
    # model.evaluate输入数据(data)和金标准(label),然后将预测结果与金标准相比较,得到两者误差并输出.
    # model.predict输入数据(data),输出预测结果
    # 2
    # 是否需要真实标签(金标准)
    # model.evaluate需要,因为需要比较预测结果与真实标签的误差
    # model.predict不需要,只是单纯输出预测结果,全程不需要金标准的参与.
    predictions = model.predict(test_dataset)
    # 通过astype()方法可以强制转换数据的类型。
    predictions = (tf.sigmoid(predictions).numpy().flatten() > 0.5).astype(int)
    print(predictions.shape, predictions)
    # 输出结果
    output = pd.DataFrame(
        {"PassengerId": passenger_id, "Survived": predictions})
    # index=False 不保存行索引,index=是否保留行索引
    output.to_csv(csv_path, index=False)
    print(f"您的提交文件保存成功! 位置在{csv_path}")
    return predictions


# 获取年月日时分秒
def get_time():
    return datetime.datetime.now().strftime("%Y%m%d%H%M")


# #### Titanic - Machine Learning from Disaster

if __name__ == "__main__":

    # 1. 导入数据
    path_url = r".\titanic\train.csv"
    test_path_url = r".\titanic\test.csv"

    raw_train_dataset, raw_test_dataset = load_data(path_url, test_path_url)

    # 2. 数据预处理
    features_test = [
        "PassengerId",
        "Pclass",
        "Sex",
        "Fare",
        "Age",
        "SibSp",
        "Parch",
        "Embarked",
    ]
    features_train = features_test + ["Survived"]

    # 获取预处理后的训练集和标签
    train_dataset, labels = preprocess(raw_train_dataset, features_train)

    # 3. 训练
    model = train(train_dataset, labels, epochs=256, is_plot=True)

    # 获取预处理后的测试集和序号
    test_dataset, passenger_id = preprocess(
        raw_test_dataset, features_test, train=False
    )

    # 输出预测结果
    csv_path = f"./submission_{get_time()}.csv"
    prediction = predict_out(model, csv_path)

    # 验证与原始数据raw_test_dataset长度是否一致
    if prediction.shape[0] == raw_test_dataset.shape[0]:
        print(f"--预测长度={prediction.shape[0]}校验通过 √")
    else:
        print(
            f"--预测长度与raw_test_dataset长度不一致 ×,prediction.shape={prediction.shape},raw_test_dataset.shape={raw_test_dataset.shape}"
        )
