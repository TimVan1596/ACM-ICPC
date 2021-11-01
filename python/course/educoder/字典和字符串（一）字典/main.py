def Read(path):
    city_dict = {}

    with open(path, 'r') as file:
        file_lines = file.readlines()
        for lines in file_lines:
            line = lines.strip().replace('\n', '').replace('\r', '')
            line_split = line.split(':')
            city = line_split[0].strip()
            tempe = float(line_split[1].strip()).__round__(1)
            city_dict[city] = tempe

    return city_dict


if __name__ == "__main__":

    path = ''
    dat = Read(path)
    for s in range(3):  # 每次评测有三次查询
        name = 'Berlin'
        if name in dat:
            print(dat[name])
        else:
            print("没有%s城市的温度数据" % (name))
