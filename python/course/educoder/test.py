def Parse():
    path = "step2/oxforddata.txt" #文件路径

    #将文件内容解析成一个多级字典，并返回
    #   请在此添加实现代码   #
	# ********** Begin *********#
    temp_dict = {}
    with open(path,'r') as f:
        lines = f.readlines()
        lines = lines[7:]
        for line in lines:
            arr = line.split()
            year = int(arr[0])
            mm = int(arr[1])
            tmax = float(arr[2])
            tmin = float(arr[3])
            af = float(arr[4])
            rain = float(arr[5])
            sun = arr[6]
            if sun == '---':
                sun = None
            m_dict = {
                'tmax' : tmax,
                'tmin' : tmin,
                'af' : af,
                'rain' : rain,
                'sun' : sun
            }
            temp_dict[mm] = m_dict
    return temp_dict


	# ********** End **********#
