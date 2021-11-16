class fractionSum:
    def peven(self, n):
        i = 0
        s = 0.0
        for i in range(2, n + 1, 2):
            s += 1.0 / i
        return s

    def podd(self, n):
        s = 0.0
        for i in range(1, n + 1, 2):
            s += 1.0 / i
        return s

    def dcall(self, fp, n):
        s = fp(n)
        return s


# 本关的测试文件给出了一个类fractionSum，此类的作用是当输入一个数n，如果n为偶数，求1/2+1/4+...+1/n的和，如果输入n为奇数，求1/1+1/3+...+1/n的和。
#
#
# 在fractionSum中，定义了方法peven(self,n)用来求当n为偶数时的结果，定义了podd(self,n)用来求当n为奇数时的结果，定义了dcall(self,fp,n)方法来调用peven与podd两个方法，fp为方法名，最后返回计算结果。
#
#
# 本关的编程任务是补全fractionSum.py文件中的创建实例与调用方法部分，具体要求如下：
#
# 填入创建fractionSum的实例fs的代码；
# 填入调用fractionSumtest类中dcall方法的代码，计算当n为偶数时计算的和；
# 填入调用fractionSumtest类中dcall方法的代码，计算当n为奇数时计算的和。
# 请在下面填入创建fractionSum的实例fs的代码
########## Begin ##########
fs = fractionSum()
########## End ##########
n = int(input())
fn = fs.podd
if n % 2 == 0:
    # 请在下面填入调用fractionSumtest类中dcall方法的代码，计算当n为偶数时计算的和
    ########## Begin ##########
    fn = fs.peven, n
########## End ##########
else:
    # 请在下面填入调用fractionSumtest类中dcall方法的代码，计算当n为奇数时计算的和
    ########## Begin ##########
    pass
sum = fs.dcall(fn, n)

########## End ##########
print(sum)
