import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from keras import models, layers
import seaborn as sns


# 导入数据
def load_data(path):
    train_data = pd.read_csv(path)
    return train_data
    title_line = train_data.columns
    df = pd.DataFrame(train_data)
    survive = df["Survived"]
    static_data = survive.value_counts()
    plt.hist(survive, bins=5, color="skyblue")
    corr_metrix = df.corr(method="pearson")
    sns.heatmap(
        corr_metrix, annot=True, cmap=palettable.cmocean.diverging.Curl_10.mpl_colors
    )
    plt.show()

    plt.savefig("result.jpg")


# 建立模型
def gen_model(x, y):
    model = models.Sequential()
    model.add(layers.Dense(32, activation="relu"))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(32, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["AUC", "sparse_categorical_accuracy"],
    )
    record = model.fit(x, y, batch_size=512, epochs=2048*4)
    return model, record


# 数据预处理
def preprocess(train_data, is_Test=False):
    # 'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
    # 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
    # fare = 旅客票价
    # parch	 = # of parents / children aboard the Titanic
    x_train = []
    y_train = None
    if is_Test is False:
        y_train = train_data.values[:, 1]
        y_train = y_train.tolist()
        y_train = tf.constant(y_train, dtype=tf.float32)
    else:
        y_train = []
    # 数值化
    train_data["Cabin"] = pd.factorize(train_data.Cabin)[0]

    train_data["Age"] = train_data["Age"].fillna(train_data["Age"].mean())
    for index, row in train_data.iterrows():
        Pclass = float(row["Pclass"])
        Parch = float(row["Parch"])
        SibSp = float(row["SibSp"])
        Fare = float(row["Fare"])
        Sex = 1.0 if row["Sex"] == "male" else 0.0
        Age = float(row["Age"])
        Cabin = float(row["Cabin"])
        Embarked = 1
        if row["Embarked"] == "Q":
            Embarked = 2
        elif row["Embarked"] == "S":
            Embarked = 3
        data = [Pclass, Parch, SibSp, Sex, Age, Fare, Cabin, Embarked]
        x_train.append(data)
        if is_Test is not False:
            y_train.append(int(row["PassengerId"]))
    x_train = tf.constant(x_train, dtype=tf.float32)

    return x_train, y_train


def predict_export(test_x, PassengerIds):
    ret = model.predict(test_x)
    Survived = []
    for item in ret:
        if item > 0.5:
            Survived.append(1)
        else:
            Survived.append(0)
    print(len(Survived))
    print(len(PassengerIds))
    submission = pd.DataFrame(
        {"PassengerId": PassengerIds, "Survived": Survived}
    )
    submission.to_csv("titanic-submission.csv", index=False)

if __name__ == "__main__":
    # 1. 导入数据
    path = r".\titanic\train.csv"
    train_data = load_data(path)
    # 2.  数据预处理
    x_train, y_train = preprocess(train_data)
    # print("@x_train=", x_train.shape())
    # print("@y_train=", y_train.shape())
    model, record = gen_model(x_train, y_train)
    loss = record.history["loss"]
    sparse_categorical_accuracy = record.history["sparse_categorical_accuracy"]
    print(x_train)
    # df = pd.DataFrame({"loss": loss, "val_loss": val_loss})
    df = pd.DataFrame({"acc": sparse_categorical_accuracy})
    sns.scatterplot(data=df)
    sns.lineplot(data=df)
    plt.savefig("result.jpg")

    path = r".\titanic\test.csv"
    # 进行预测
    text_data = load_data(path)
    test_x, PassengerIds = preprocess(text_data, is_Test=True)
    predict_export(test_x, PassengerIds)

    pass
