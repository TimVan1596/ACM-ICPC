def Parse():
    path = "oxforddata.txt"  # 文件路径

    # 将文件内容解析成一个多级字典，并返回
    #   请在此添加实现代码   #
    # ********** Begin *********#
    # 对数据进行预处理，取出*号和---等
    def proc_value(value: str):
        value = value.strip()
        value = value.replace('*', '')
        if '---' in value:
            value = None
        elif '.' in value:
            value = float(value)
        else:
            value = int(value)
        return value

    temp_dict = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = lines[7:]
        for line in lines:
            arr = line.split()

            year = proc_value(arr[0])
            mm = proc_value(arr[1])
            tmax = proc_value(arr[2])
            tmin = proc_value(arr[3])
            af = proc_value(arr[4])
            rain = proc_value(arr[5])
            sun = proc_value(arr[6])

            m_dict = {
                mm: {
                    'tmax': tmax,
                    'tmin': tmin,
                    'af': af,
                    'rain': rain,
                    'sun': sun
                }
            }

            temp_dict.setdefault(year, {})
            temp_dict[year].update(m_dict)

    return temp_dict

    # ********** End **********#


if __name__ == "__main__":
    dat = Parse()

    print(dat)

    n = int(3)
    for s in range(n):
        cmd = '1853 1 tmax'.split()
        y = int(cmd[0])
        m = int(cmd[1])
        print(dat[y][m][cmd[2]])
