import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
#  不要改变上面的顺序

import datetime


def Draw():
    appl = "AAPL.csv"  # 苹果
    google = "GOOG.csv"  # 谷歌
    ms = ".csv"  # 微软

    appl = auto_path(appl)
    google = auto_path(google)
    ms = auto_path(ms)

    # 在此绘制折线图
    #   请在此添加实现代码   #
    # ********** Begin *********#
    # 初始化plt绘图
    # plt.xlim((2014, 2019))
    plt.ylabel('Open')
    # plt.ylim((0, 1200))
    # arr = [i for i in range(0, 1201, 200)]
    # plt.yticks(arr)
    plt.xticks(rotation=45)  # x轴的刻度数值，45度倾斜

    appl = ['Appl', appl, 'red']
    google = ['Google', google, 'green']
    ms = ['Microsoft', ms, 'blue']
    result = {}
    file_path_list = [appl,google,ms]
    for file_path in file_path_list:
        data = read_csv(file_path[1])
        result[file_path[0]] = data
        # print(result[file_path[0]])

        # 获取横轴和纵轴，并把日期格式化
        dates = list(data.keys())
        dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
        opens = list(data.values())
        plt.plot(dates, opens, linewidth=1.0, color=file_path[2], label=file_path[0])

    plt.legend(loc='upper left')

    # ********** End **********#
    # plt.show()
    plt.savefig("data.png")


# 如果有必要，可以增加别的函数协助完成任务，可在此添加实现代码
# ********** Begin *********#
def auto_path(path):
    return '/'.join(path.split('\\'))


# 对csv的内容进行解析，返回date:open的字典
def read_csv(path):
    info_dict = {}

    with open(path, 'r') as file:
        file_lines = file.readlines()
        for index in range(1, len(file_lines)):
            line = file_lines[index]
            line = line.strip().replace('\n', '').replace('\r', '')
            line_split = line.split(',')
            Date = line_split[0]
            Open = float(line_split[1])
            info_dict[Date] = Open
    return info_dict


# ********** End **********#



if __name__ == "__main__":
    Draw()
