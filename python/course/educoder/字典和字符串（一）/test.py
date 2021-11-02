def Read(path):
    with open(path,'r') as file:
        print(file.readlines())



	# ********** End **********#


path = '.\data.txt'
dat = Read(path)
for s in range(3):#每次评测有三次查询
    name = input()
    if(dat.has_key(name)):
        print(dat[name])
    else:
        print("没有%s城市的温度数据" % (name))