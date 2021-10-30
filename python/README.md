#### 路径
1. 【学习】Python基本语法（8次）  √
2. 【练习】LeetCode(19次)     √
    &emsp;&emsp;&emsp;&emsp;Python3 迭代器与生成器     √  
    &emsp;&emsp;&emsp;&emsp;Python3 模块  
    &emsp;&emsp;&emsp;&emsp;Python3 输入和输出     √    
    &emsp;&emsp;&emsp;&emsp;Python3 File(文件) 方法     √    
    &emsp;&emsp;&emsp;&emsp;Python3 OS 文件/目录方法     √     
    &emsp;&emsp;&emsp;&emsp;Python3 错误和异常     √  
    &emsp;&emsp;&emsp;&emsp;Python3 面向对象     √  
    &emsp;&emsp;&emsp;&emsp;Python3 命名空间和作用域     √  
3. 【学习】爬虫技术
4. 【练习】爬虫项目
5. 【学习】机器学习
6. 【练习】图片分类

学习+练习 三七开

#### 笔记
index = 10
##### 1.格式化输出
    1. 输出和C语言不同，使用print('%d' %( var ))形式(！：%前没有逗号)
    2. ("Bill", "Jobs", "Jack", sep="-", end="\t")
        sep 为多个的连接符，end为结束后的字符      
##### 2. input
    python使用 ret = input("提示语\n") 进行输入
##### 3.  type()
    相当于typeof
##### 4.  随机数
    random.randint(0,2),范围为双闭区间[0,2]
##### 5.  强制类型转换
    int(action) ，int不需要大括号
##### 6.  逻辑运算符 
    由 &&，||，! 改为 and, or, not
##### 7. 变量两边范围
    由 (a>100) && (a<=200) 改为 100< a <=200
##### 8. 循环的边界
    for i in range(7) , 0 <= i < 7 , 左闭右开区间
##### 9. 自增和自减
    Python 中没有 i++ 和 i-- 
##### 10. "-"*5
    输出5个“-”字符
##### 11. append和extend
    append是将参数作为一个元素插入到List中
    extend是将另一个List中的元素逐个插入到原List中
##### 12. 列表删除项
    del namelist[2] 形式，不是函数形式
    List.remove()根据传入参数，查找相同参数内容的首个下标位置元素进行删除
##### 13. 列表访问相关
    namelist[-2] 是访问下标倒数第二个的元素
    namelist[1:4] 是访问 [1,4) 下标范围内的元素
##### [14].字典访问不存在的数据
    myDict.get('name','Empty Name')，函数的第二个参数为值不存在时的默认值
##### 15.多个返回值
    python中支持多个返回值，如
```
def fun():  
    return 3,4
a,b = fun()
```
##### 16.函数中使用全局变量
    函数中，需要先使用global a 进行声明，注意需要在首行如：
```    
a = 2020
def test():
    global a    //如注释此行，外部打印则依旧为2020
    a = 33
    print("in test(),a={}".format(a))

test()
// 打印结果为 in test(),a=33 --- in outer, a=33
print("in outer, a={}".format(a))
```
##### 17.异常处理获得错误原因
```
    try:
        print(a)
    except NameError as reason:
        print("reason:%s" % reason)
```
##### 18.&、| 和 and、or 运算符
    当两边为逻辑表达式时，如(a > b) & (b > c)时
    两套符号等同
    当两边为数值，如 47 & 16时
    &和|作为与运算、或运算，and和or的结果为左右两边起决定性的一边
    如 (0 or 16) =  16
##### 19.数列中寻找符合条件的两个数
    可以遍历数列并加入**哈希表**中，Key为数字，Value为序号，当求得后一个数时，直接查找key是否在表中，节省双重循环。
##### 20.三目表达式
    python仅支持c = a if a>b else b
##### 21.break语句和while..else..
    循环体中有break、return和异常进行退出时，不会进入else子句
##### 22. //=
    除法，向下取整，如 a = 50，a //= 3，结果a为16
##### 23. 负数取余
    python中负数取余结果为正，即取正余数
    如：a = -11%4 , a = 1
    其中 -11 = 4*(-3) + 1
    在C++和Java中取得负余数
    其中 -11 = 4*(-2) -3
##### 24.乘方
    2**32 表示 2的32次方
##### 25.枚举的序号
    序号默认从0开始，若enumerate(list, start=10)，可改变序号，如：
```
    list = [2020, '天青釉汝窑', True]
    print(list)
    myEnum = enumerate(list, start=10)
    for i, content in myEnum:
        print("{} : {}".format(i, content))
```
##### 26.代码换行
    python中的换行需要 '\' 符号
    条件语句的换行应在关键字and,or前，尽量使用IDE换行
##### 27.考虑下一个元素是否存在
    当遍历集合需要考虑下一个元素是否存在时，可以尝试倒序访问
##### 28.zip()
    zip()可将N个数列的对应下标打包，并可以转换成元组列表
    zip(*)将列表对应位解压成元组集合，相当于反操作
    如：
    list1 = ["Tim", "Jobs", "Steve", "Bill"]
    for one in zip(*list1):
        print(one)
    # 输出结果
    # ('T', 'J', 'S', 'B')
    # ('i', 'o', 't', 'i')
    # ('m', 'b', 'e', 'l')
##### 29.set()
    将可迭代对象如列表转化为集合
    可使用 len(set(list1)) 判断列表不重复元素的个数
##### 30. list.pop()的参数
    将要弹出的元素的下标，默认为-1（最后一个）
##### 31. 匹配判断
    需要匹配取余时可直接将元素取余，判断个数。
    如判断括号匹配时，字符串是"[()]{"，则待匹配元素个数为5，
    是奇数即直接非法。
    注意：是待判断元素的个数
##### 32.range()参数
    range(stop)
    range(start, stop[, step])
    第二个重载相当于到stop结束，但不包括stop，step为步长
    for i in range(0,7,2) 相当于 for(int i=0; i<7; i+=2)
##### 33.边遍历边删除（添加）
    遍历数组时对元素删除或添加时，由于数组长度变化，导致指示下标的变化。因此可用从后往前遍历，可以简化修正下标的操作。
##### 34.index()和find()
    当字符串含子串时，均返回首字符下标。
    当不含子串时，index()会产生异常，而find()会返回-1。
    若子串为空，均返回0。
    find()不可用于list类型。
##### 35.已知数组长度进行初始化赋值
    若数组长度为arrLen，初始化赋值为value
    有两种方式：
    ① arr = [value] * arrLen
    ② arr = [value for i in range(arrLen)]
##### 36.打印输出bool
    使用%s可输出True和False
    使用%d可输出1（真）和0（假）
##### 37.动态规划=子问题
    将最终的大问题，化为有重复的子问题。
    需要让子问题不要重复计算，而提前保存下来。
    这种方法就叫做动态规划。
    p.s. “动态规划”的名字比较有迷惑性，应理解为“去除子问题重叠”方法
##### 38.分别赋值
    a = 10
    b = 20
    a, b = b, a + b
    即a = b和b = a+b
    需要特别注意的是，结果为a=20，b=30。
    说明a和b在赋值时是同时进行，a和b值并未有改变的顺序。
##### 39.Pycharm导入自定义模块出现错误
    无其他错误下不影响运行。若想去除错误红线，
    可以模块所在目录Mark dic as 根目录去除。
##### 40.路径问题
    进入当前目录下的文件夹"test\\test.txt"、"test\copy.txt"
    其中注意：
    ①test文件夹前不需要反斜杠\
    ②注意\t的转义
##### 41. {0}{1}.format
    使用   '{0}:{0} lived in {1}'.format(name, nation) 形式，可以实现变量重复使用
##### 42. print(10/3)
    打印结果为：3.3333333333333335
##### 43. \_\_name\_\_
    在当前运行文件下为__main__
    若为被引入文件下为被引入的文件名
##### 44. urllib
    注意请求和接收
```
    req = urllib.request.Request(url=douBanUrl
                             # , data=data
                             , headers=headers
                             # , method="post"
                             )
    response = urllib.request.urlopen(req)
```
---
##### 45. python没有switch..case
    