#模块
'''
###############################################################模块导入###############################################################

模块编写完成就可以被其他模块运行调用并使用被调用模块中的功能
import导入方式的语法结构:
import 模块名称 [as 别名]

form ... import导入方式的语法结构:
form模块名称import 变量/函数/类/*
此时不用使用模块前缀，直接使用对应的变量和函数即可
*为导入模块中所有（*为通配符）

一次导入多个模块，模块间可以使用英文逗号间隔

import mk as m

m.infort()

# Other 模块  #为main函数中
# 模块导入


print(m.t)

# tttttt



from mk import t
from mk import infort

infort()
print(t)

# 模块导入
# tttttt


from mk import *

print(t)

infort()

# tttttt
# 模块导入


#同时导入多个
import time,math,random




def f(x):
    pass
class A:
    pass
print('单个模块')

#自定义模块，创建一个py文件就是创建一个模块了
#导入模块


import math
print(id(math))
print(type(math))
print(math.pi)
print('-----------------------------'
      )
print(dir(math))
# from 模块名称 import 函数/变量/类
from math import pi#直接导入math中一个变量
print(pi)

import mk
print(mk.f(3))




1781815356336
<class 'module'>
3.141592653589793
-----------------------------
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
3.141592653589793
Other 模块
9


#导入模块中含有同名的变量和函数，后导入的会将之前导入的进行覆盖

from day_11_21 import *
from mk import *

#两个均有t这个变量


print(t)
#此t为mk中变量，而非day...中变量
# Other 模块
# tttttt


#如果不想覆盖,可用import
# 可以使用import二不适用from。。。import

import day_11_21
import mk

print(day_11_21.t)
print(mk.t)

# 666
# tttttt



#############################################################模块和包的区别##############################################################
python中的包：
含有__init__.py文件的文件夹（目录）
可以避免模块名称相冲突问题

主程序运行
if__name__== '__main__':  #均双下划线
   pass

'''
print(format('模块和包的区别','#^130'))
'''

#学生信息管理系统11集
#15个实操案例
#144-167=24
#包为分层次的目录结构，它将一切功能相近的模块组织在一个目录下
#import bag1.m1,bag1.m2#bag为包，包中有很多模块

import bag1.m1 as bm1#为了简略,可以用as来换掉变量名

print(bm1.a)#,bag1.m2.b)

#导入包中模块或者变量可以通过以下
from bag1 import m1#导入模块
from bag1.m1 import a#导入变量

#python中常用内置模块
sys 与python解释器及其环境操作相关的标准库
time 提供与时间相关的各种函数的标准库
os 提供访问操作系统服务功能的标准库
calendar 提供与日期相关的各种函数的标准库
urllib 用于读取来自网上（服务器）的数据标准库
json 用于使用JSON序列化和反序列化对象
re 用于在字符串中执行正则表达式匹配和替换
math 提供标准算数孕栓函数的标准库
decimal 用于进行精确控制运算精度，有效数位和四舍五入操作的十进制运算
logging 提供了灵活的记录事件，错误，警告和调试信息等日志信息的功能

import sys,time,urllib

#print(sys.getsizeof(24))
#print(sys.getsizeof(99))
print(time.time())#现在时间的秒形式
print(time.localtime(time.time()))



###############################################################文件操作###############################################################


#文件操作
#encoding=UTF-8
#第三方模块的安装与使用

import time

i=1
while 1:
    print(i)
    i=i+1
    time.sleep(0.5)
#！！！！！！！！！！！！！！！！！！打开系统窗口 win+R  输入pip install +安装包名即可安装外来库！

import time
i=0
while True:
   file2=open('E:/新建文件夹 (2)/file2.txt','a+')
   print('hello world',file=file2)
   file2.close()
   time.sleep(0.5)
   i+=1
   if i>100:
       break
二进制文件，需要用到专门的软件打开，如mp3,jpg,doc等文件
r 只读模式（read）
w 只写模式，若文件不存在，则创建，若存在则覆盖原有内容
a 以追加模式打开文件，不存在时创建，存在则在末尾最佳内容
b 以二进制方式打开文件，需要与其他一起使用如rb wb
+ 以读写方式打开文件，不能单独使用要配合如a+



i=0
file=open('E:/新建文件夹 (2)/file.txt','r')
#print(file.readlines())
for x in file.readlines():
   print(x)

   i=0
f=open('E:/新建文件夹 (2)/file.txt','w')
while True:
   if i > 100:
      break
   print(i, file=f)
   i += 1
f.close()
with open('E:/新建文件夹 (2)/file.txt','w') as z:
   print(z.write('nihao'))

#with 可以自动管理上下文资源，with可以保证文件正确关闭，从而达到释放资源的目的
with open('E:/新建文件夹 (2)/file.txt','r') as x:
   print(x.read())#不用手动关闭文件

import os
#os.system('notepad.exe')#相当于win+R后输入notepad.exe
#直接调用可执行文件
#os.startfile(r'C:\Program Files\XMind ZEN\XMind ZEN.exe')#直接打开文件
print(os.getcwd())


'''

print(format('模块导入','#^130'))