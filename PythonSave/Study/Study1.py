#!/usr/bin/python3

import math

# ----------------------------- 注释方式 ----------------------------------------
"""
这样的注释方式很无奈，不习惯
"""
"""
感觉很无用啊，函数调用时候的注明显示貌似也看不到了
"""

# ------------------------------ 输出方式 ---------------------------------------
"""
通用的输出模式,没什么区别,
"""
# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。包含了多个语句"""
#
# print(word);
# print(sentence);
# print(paragraph);

# ------------------------------- 分号作用 --------------------------------------
"""
就目前还未看出是什么效果,另外分号的作用仅限于同一行使用，但是若是语句进行换行，完全不需要分号来作用，没任何意义
"""
# import sys;
# x = 'runoob';
# sys.stdout.write(x + '\n')
# print(x)

# -------------------------------- class -------------------------------------
"""
这只是一个测试用的class,但是功能貌似不全，如何在另外一个python里面调用这个python的class是个问题
"""
# class test2:
#     teststr = "test1";
#     print(teststr)

# -------------------------------- import导入库 -------------------------------------
"""
导入sys头文件,表示可以使用sys底层库的东西
"""
# import sys
# print("参数的个数为",len(sys.argv),'个参数')
# print("参数列表：",str(sys.argv))

# --------------------------------- 通过命名行传递参数 ------------------------------------
"""
以下为通过命名行进行参数传递进来，限于外层命名行通过python 调用脚本的使用,
并且还要查看脚本找到对应的参数对应的语法，如下列需要在命名行先属于-i的字节后才可输入对应的数值，非常不友好
表现在如果是你输入的-i字节不对，那么就无法将-i的值传递进去,并且,程序参数命名一般为拓风命名法，不可能如此短小
"""
# import sys, getopt,pdb
#
# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print ('Test1.py -i <inputfile> -o <outputfile>')
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print ('Test1.py -i <inputfile> -o <outputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print ('输入的文件为：', "inputfile")
#    print ('输出的文件为：', "outputfile")
#    print(opts)
#
# if __name__ == "__main__":
#    main(sys.argv[1:])

# ---------------------------------- 变量类型 -----------------------------------
# ---------变量赋值
"""
直接定义声明变量名,通过直接的赋值方可看出变量的类型,对表层开发方便,底层很容易出错
如字符串类型name被整型counter给赋值了,那么counter的类型就被改变了,这样对严谨的程序容易误导
"""
# counter = 100  # 赋值整型变量
# miles = 1000.0  # 浮点型
# name = "John"  # 字符串
#
# print(counter)
# print(miles)
# print(name)
#
# name = counter
#
# print(name)

# ---------多个变量赋值
"""
常规赋值方式,没什么差异
第一行输出为并行输出,第二行为换行输出,第三行为强转换行输出
"""
# a = b = c = 1
#
# d, e, f = 1, 2, "John"
# print(a, b, c, d, e, f, "\n")
# print(a, "\n", a, "\n", b, "\n", c, "\n", d, "\n", e, "\n", f, "\n")
# print(str(a) + "\n", str(b) + "\n", str(c) + "\n", str(d) + "\n", str(e) + "\n", str(f) + "\n")

# ---------Python数字
"""
这里对于数字并没有特殊的讲解
但是在对删除对象del的使用表示有疑问
1、del var1[,var2[,var3[....,varN]]]]这种方式会直接报错，后续应该有案例怎么快速删除一堆对象
2、del var_a, var_b这种方式可以删除对象，但是通过断点调试发现对象指还存在,然而打印对象值又表示值不存在,保守估计有内存泄漏的可能,用C/C++说法就是存在野指针,谨慎使用
3、del var无异议,断点调试可法相对象不存在了,也不能直接
"""
# var1 = 1
# var2 = 10cool

# del var1[,var2]

# del var1

# del var2, var1

# print(var1,var2)

# --------- Python字符串
"""
没什么好讲的,要注意的是空格占两字节
截取三参数的传递,第一个参数为截取的位置,第二个参数为截取的末尾的位置,第三个参数为相隔多少进行截取
"""

# n_Str1 = "Landis is so cool "
#
# print(n_Str1[2:10])
# print(n_Str1[2:])
# print(n_Str1 * 2)
# print(n_Str1 + "and perfect!")
# print(n_Str1[2:22:3])

# --------- Python列表
"""
注意：输出中[a:b]不是指在数组中从a到b的所有值进行输出（包括a和b下标的值）
而是从a开始,到b结束,类似乐园排队,明确指出你前面的人可以进行游玩了（列表值和数组一样，永远从0开始计算）
"""
# list = ['runood', 786, 2.23, 'john', 70.2]
#
# tinylist = [123, 'john']
#
# anymap = [1, 2, 3]
#
# print(list)               # 输出完整列表
# print(list[0])            # 输出列表的第一个元素
# print(list[1:3])          # 输出第二个至第三个元素
# print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
# print(tinylist * 2)       # 输出列表两次
# print(list + tinylist)    # 打印组合的列表
# print(anymap[:])          # 从头到尾全部打印


# ---------元组
"""
元祖类似与列表：用法差不多，唯独区别是,元组使用小括号进行声明,列表使用中括号,后续差异,以后进行罗列
"""
# tuple = ('runoob', 789, 2.23, 'John', 70.2)
# tinytuple = (123, 'john')
#
# print(tuple)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:])
# print(tinytuple * 2)
# print(tuple + tinytuple)


# -----------字典
"""
数据格式为Json格式字符串
不同的是,Python对字典里面的key、Value值的类型有所限制,可以直接赋值
最早开始讲过,没有直接对变量值的类型进行定义, 新手好上手,后期会有盲区
"""
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is tow"
#
# tinydict = {'name': 'John', 'code': 6734, 'dept': 'sales'}
#
# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

# ---------Python数据类型转换
"""
int     可转化类型:1、为整数型样式的字符串;2、浮点型
long    使用int转换，int到long为隐式转换
float   可转换类型:1、为数字了新的字符串(整数,浮点型);2、整数型
str     可转换类型:无限制
"""
# int(x [,base])          #将x转换为一个整数
# long(x [,base] )        #将x转换为一个长整数
# float(x)                #将x转换到一个浮点数
# complex(real [,imag])   #创建一个复数
# str(x)                  #将对象 x 转换为字符串
# repr(x)                 #将对象 x 转换为表达式字符串
# eval(str)               #用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)                #将序列 s 转换为一个元组
# list(s)                 #将序列 s 转换为一个列表
# set(s)                  #转换为可变集合
# dict(d)                 #创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)            #转换为不可变集合
# chr(x)                  #将一个整数转换为一个字符
# unichr(x)               #将一个整数转换为Unicode字符
# ord(x)                  #将一个字符转换为它的整数值
# hex(x)                  #将一个整数转换为一个十六进制字符串
# oct(x)                  #将一个整数转换为一个八进制字符串

"""
整数型转换
"""
# a = '123'
# print(int(a))
# b = 3.1415926
# print(int(b))
# c = -3.1415926
# print(int(c))

"""
浮点型转换
"""
# a = 132
# print(float(a))
# b = "12.5"
# print(float(b))
# c = -123
# print(float(c))
# d = "-12"
# print(float(d))

"""
字符串转型
"""
# a = 123
# print(str(a))
# b = 3.1415926
# print(str(b))
# c = -123
# print(str(c))
# d = -3.1415926
# print(str(d))
# print(str(complex(1, 2)))

"""
# 循环语句
# 八皇后
"""

# BOARD_SIZE = 8
#
#
# def under_attack(col, queens):
#     left = right = col
#     for r, c in reversed(queens):
#         left, right = left + 1, right + 1
#         if c in (left, col, right):
#             return True
#
#
# def solve(n):
#     if n == 0:
#         return [[]]
#     smaller_solutions = solve(n - 1)
#
#     return [solution + [(
#         n,
#         i + 1)]
#
#         for i in range(BOARD_SIZE)
#         for solution in smaller_solutions
#         if not under_attack(i + 1, solution)]
#
#
# for answer in solve(BOARD_SIZE):
#     print(answer)

"""
循环语句常用手法方式
"""
# def deduplication(self, nums):
#     # 循环1：将列表进行循环查找，找到即可返回值并跳出循环
#     for i in range(len(nums)):
#         if nums[i] == self:
#             return i
#
#     # 循环2：将列表值全部循环,对比大小,若超出大小,即前一下标值为答案
#     i = 0
#     for x in nums:
#         if self > x:
#             i += 1
#     return i
#
#
# print(deduplication(5, [1, 3, 5, 6]))


"""
使用列表罗列偶数
"""
# doubleNums = []
#
#
# def getDoubleNum(count):
#     a = 1
#     while a < count:
#         doubleNums.append(a)
#         a += 2
#
#     return doubleNums
#
#
# print(getDoubleNum(20))


"""
循环语句查找质数
"""
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num/i
#             print('%d 等于 %d * %d' % (num, i, j))
#             break
#
#     else:
#         print(num, '是一个质数')

"""
数学语法调用
1
"""
#
# a = 1
# b = 2
#
# if(math.cmp(a, b))

"""
2
"""
# a = 30
# b = 20
#
# print((a > b) - (a < b))

"""
2
"""
# a = -10
# print(abs(a))
"""
3
"""
# a = 3.1415926
# print(math.ceil(a))


"""
键盘keyboard输入控制监视
游戏1
"""
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# # input("点击 enter 键退出")

"""
游戏2
"""
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

"""
迭代器与生成器
斐波那契
"""
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

"""
死循环异常抛出
"""
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
#

"""
方法体（函数）声明
"""
# def priHello():
#     print("Hello world")
#

# priHello()

"""
可写函数传参：参数为列表
"""
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# print("函数外取值: ", mylist)
# changeme(mylist)


"""
函数声明,不限制参数个数与声明
"""
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple[0])
#
#
# # 调用printinfo 函数
# printinfo(70, 60, 50, 40, 30, 20)

"""
lambda函数声明,与常规lambda函数有差异
常规lambda函数方法体是可以进行正常的逻辑运行,此处表现不行
后期查看具体优势
"""
# sum = lambda arg1, arg2: arg1 + arg2
#
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))


"""
标量作用域
"""
# def fun1():
#     global num
#     num = 1
#     print(num)
#     num = 123
#     print(num)
#
# # num = 1
# fun1()
# print(num)

"""
推导式
"""
# vec = [2, 4, 6]
# print([3*x for x in vec])
# print([[x, x**2] for x in vec])


"""
导入模块
前期提到的从其他调用写好的函数，使用里面的逻辑
"""
# import support
#
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")

"""
关于__name__的使用,后期双调进行说明
"""
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')

"""
open(filename, permissious):filename->路径名称, permissious->权限等级
open会根据路径进行查找,若查找到了会进行赋值加载,若无,则在路径下创建该文件
请一定确保路径正确性,或者os优先验证路径文件是否存在
"""
# a = open("E:/CC_APK/Test.txt", "w+")
# a.write("Landis is so perfect!\nYes")
# a.close()
#
# f = open("E:/CC_APK/Test.txt", "w+")
# print(f.read())
# f.close()

"""
os功能一，判断路径文件是否存在
"""
# import os
#
# a = os.path.exists("E:/CC_APK/Test.txt")
# print(a)

"""
数据加密1：MD5
使用范围:获取两段同为MD5加密数据进行对比,如设备号或者用户帐号对比等
纯加密：不适用Excel数据加密,后续前端解密获取对应数据
"""
# import hashlib
#
# h = hashlib.md5()
# str = 'boboadmin'
# h.update(str.encode())
# msg = h.hexdigest()
# print(msg)

"""
数据加密：SHA1
作用效果与MD5一致
但是由于时间换取安全性,因此比MD5更加安全
"""
# import hashlib
#
# sha = hashlib.sha1()
# data = 'Landis is cool'
# sha.update(data.encode('utf-8'))
# sha_data = sha.hexdigest()
# print(sha_data)

"""
数据加密：Base64
可方式是为像是加密的编码,所以才称base64是伪加密,知道若有对应字符编码很容易被破解
因此若知道对应的字符编码因此也容易被破解,但若不知道,强行使用decode解密会报错
所以前面若非知道对应字符编码,不可轻易使用decode转化
"""
# import base64
#
# str = '我们一起打豆豆'
# str = str.encode('utf-8')
# # 加密
# bs64 = base64.b64encode(str)
# print(bs64)
# # 解密
# debs64 = base64.b64decode(bs64).decode('utf-8')
# print(debs64)

"""
数据加密
"""





