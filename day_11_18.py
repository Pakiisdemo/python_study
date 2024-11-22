'''
程序描述方式
1自然语言（IPO格式）
输入：。。。。
处理。。。。。。
输出。。。。。

2流程图
起止框
判断框
处理框
等

3伪代码

===============================================程序组织结构
顺序结构
选择结构
循环结构

#顺序结构
语句A
语句B

从上到下依次执行每一条

print('赋值语句')
print('输入输出语句')
print('模块导入语句')



a,b,c,d='room'
print(a,b,c,d,sep='------>')

r------>o------>o------>m
等

#分支对象的布尔值
#选择结构   （多分枝结构）

如果表达式的值位True就执行语句块，表达式值位False则跳过语句块
if  表达式:
    语句块

非常重要（冒号和缩进）


===========================================================================
>
<
==
!=
>=
<=
结果为bool类型
==========================================================================
只要表达式位True（不是空字符串或者数值0等）
就可执行语句块

双分支结构
if 表达式:
    语句1
else:
    语句2   


level=int(input('输入待比较数字'))
if level>66:
    print('输入数大')
else:
    print('输入数小')

输入待比较数字99
输入数大

多分枝结构
if 表达式1:
    语句块1
elif  表达式2:
    语句块2
elif  表达式3:
    语句块3
   ...
else:
    语句块n


a=input('第一个数')
b=input('第二个数')
if  a>b :
    
elif b>55:
    print('a<b')
#else:#怎么跳出循环呢？？？   ///最后个else 可省略
   # print('a=b')
    
a=int(input('第一个数'))
b=int(input('第二个数'))
if  a>b :
    if b>55:
        print('a,b均大于55')
    elif a>55:
        print('a>55,b<55')
    else:
        print('a,b均小于55')
else:
    if a>66:
        print('a,b均大于66')
    elif b>66:
        print('b>66,a<66')
    else:
        print('a,b均小于66')

第一个数56
第二个数77
b>66,a<66

多分枝可以用来判断数值区间
比如评分A B C D E等

单分支，双分支嵌套使用
内层分支可作为外层分支的语句块使用

print('-'*130)                  #130刚好铺满
----------------------------------------------------------------------------------------------------------------------------------
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%嵌套的不会写！！！！！！！%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

a=input('第一个数')
b=input('第二个数')

if a>10|b>5:

       if a>b:
           print('a>b')
       else:
           print('a<b')
else:
    print('bufuhe')


    print('hello world')
#if 语句的嵌套使用

#酒驾测试
a=input('喝酒了码：y/n')
if a=='y':
       #测试酒精浓度
       b=int(input('酒精浓度：'))
       if b>80:
           print('醉驾')
       else:
           print('酒驾')
else:
    print('正常')
    print('hello world')
    
喝酒了码：y/ny
酒精浓度：99
醉驾


a=int(input('输入第一个数：'))
b=int(input('输入第二个数：'))

if a>b:
    print('a>b\n')
    if b>10:
        print('b>10')
    else:
        print('b<10')
else:
    print('a<b')

#条件表达式， if else 的简写

#A   if  条件   else    B


a=int(input('输入第一个数：'))
b=int(input('输入第二个数：'))
print('a>b'     if a>b else     'a<b' )

a='12'
b='13'
print(a+'小于'+b)#只有str类型才可以进行+号连接


==========================================多个条件判断
使用bool运算符
and  多个条件同时满足才位True   即才会执行后面语句块

a=input('用户名：')
b=input('密码：')

if a=='hello' and b=='666':  #此处用==不要用=
    print('pass')
    
用户名：hello
密码：666
pass


or链接则只要有一个满足则位True   即会执行后续语句块

a=int(input('成绩：'))

if 0>a or a>100:
    print('成绩无效')
elif  40<a  and a<50:
    print('E')
elif  a<60:
    print('D')
elif  a<70:
    print('C')
elif  a<80:
    print('B')
elif  a<90:
    print('A')
else:
    print('A+')    

成绩：99
A+

=============================================================循环结构==================================================================
1 遍历循环结构 for
2 无限循环结构 while
    
模式匹配
match 匹配对象:
   case 要匹配对象1:
        语句块
   case 要匹配对象2:
        语句块

        a=input('成绩等级：')

match  a:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')

需要python3.10或者更高版本



遍历结构  for语句结构

for 循环变量 in 遍历对象:
    语句块
--------------------------------
遍历对象中是否有元素
有 则取一个元素（赋值给循环变量）
执行语句块

没有则跳过
-------------------------------

for in 循环

in 表达从字符串，序列中依次取值，遍历
for in 的遍历对象必须是可迭代的对象

range()函数用于产出一个[n,m){包含n但是不包含m的整数序列}

#range()函数
print(list(range(10)))#创建一个2~stop之间的整数序列，步长为1
print(list(range(1,10)))#创建一个star到stop中间的序列步长为1
print(list(range(1,20,1)))#创建一个star到stop中键序列，步长自定
#range(函数不会序列到其上输入的数，而是以它为界限。)
#判断是否就存在，用 in   not in
print(2 in list(range(2,10)),2 not in range(2,10))
#range(函数优点，不管对象序列多长，range对象所占用空间均相同)应为只需要存储star和stop，当调用时，序列中元素才会被计算出来（是不是运行时间长？）


for i in range(100):#取出的每一个元素均赋值给i
    print(i)
    if i>95:#注意这里的次数，时在执行一遍还是立即跳出,立即跳出
        break
        
...从0开始
90
91
92
93
94
95
96        

可以遍历字符串


for item in '好好学习，今天也要好好好学python啊':
    if item=='，':
        continue  #切断后续执行，直接回归主执行
    print(item)#可不可以一行输出呢？？？？要用到转义字符吗？

 好
好
学
习
今
天
也
要
好
好
好
学
p
y
t
h
o
n
啊  
for...else...结构     {可用于执行完循环后输出循环结果}

for 循环变量 in 遍历对象:
    语句块1
else:
    语句块2

    
for i in range(100):

    if i>100:
        break
    print(i)
else:
    print('100输出完毕')#俩效果不是一样？？？，可能是用在许多语句时候用的把吧！不至于会直接运行其他结果而运行这一个独有的结果
#print('100输出完毕')

...
95
96
97
98
99
100输出完毕

#大嵌套循环；for in  if else   while   一起进行嵌套循环
    

#while循环结构
无限循环结构while语句结构   表达式位True才会执行下列语句块，False则不会执行语句块
while 表达式:
    语句块


while循环的四个步骤
1)初始化变量
2)条件判断
3)语句块
4)改变变量


while...else...结构

while 表达式:
    语句块1
else:
    语句块2

#else 语句可与if  while  for  语句进行搭配使用

i=0
anser=input('y/n：')
while  anser=='n':
    i+=1
    print('上课day+',i)
    anser=input('y/n:')

y/n：n
上课day+ 1
y/n:n     
上课day+ 2
y/n:n     
上课day+ 3
y/n:n     
上课day+ 4
y/n:n
上课day+ 5
y/n:n
上课day+ 6
y/n:n
上课day+ 7
y/n:n
上课day+ 8
y/n:y

i=1
a = 1
while a<1000 :  #True蔡虎执行
    #whil  会执行n+1次，条件为true时还会多执行一次，，if 判断一次，为true执行一次
   a+=1
 print(a)

2
...
995
996
997
998
999
1000


a = 1
while a<1000 :
    #whil  会执行n+1次，条件为true时还会多执行一次，，if 判断一次，为true执行一次
    print(a)
    a+=1

1
...
997
998
999

#计算1~100之间偶数和
i=1
sum=0
while i<100:
        if i%2==0:
            sum += i
        i += 1
print(sum)

2450




i=0
sum=0
while i<100000:#为true 才会执行
    print(i)
    i+=1
else:
    print('100000输出完毕')

0
...
99995
99996
99997
99998
99999
100000输出完毕

else用于循环结束后输出或者执行
可以直接else输出循环结果


循环嵌套

while  ...:
    for ..in ...:
    else:
        
    
    if ..:
        pass
    else:
        pass
        
        #这样嵌套循环！while  if  和for 语句进行嵌套循环！
    
for i in range(1,4):
    for j in range(4):
        print('*',end='\t')
    print()
    #二层循环中嵌套循环的break和continue ，break结束整个内层循环跳入后续外层循环中，continue会结束当前语句的后续部分重开当前语句



程序跳转语句
break用于跳（退）出循环结构，通常于if连用
语法结构
while 表达式1:
     执行代码
     if 表达式2:
       break

break直接从if程序中跳转到while中条件判断位False的语句中（即直接跳出while循环，执行下一段程序）

i=0
while  i<1000:
    print(i)
    i+=1
    v=input('输入数值看是否要结束')
    if v=='5':
        print('继续')
    else:
        break

0
输入数值看是否要结束5
继续
1
输入数值看是否要结束5
继续
2
输入数值看是否要结束5
继续
3
输入数值看是否要结束5
继续
4
输入数值看是否要结束5
继续
5
输入数值看是否要结束5
继续
6
输入数值看是否要结束5
继续
7
输入数值看是否要结束5
继续
8
输入数值看是否要结束5
继续
9
输入数值看是否要结束5
继续
10
输入数值看是否要结束5
继续
11
输入数值看是否要结束5
继续
12
输入数值看是否要结束5
继续
13
输入数值看是否要结束5
继续
14
输入数值看是否要结束5
继续
15
输入数值看是否要结束5
继续
16
输入数值看是否要结束5
继续
17
输入数值看是否要结束5
继续
18
输入数值看是否要结束5
继续
19
输入数值看是否要结束5
继续
20
输入数值看是否要结束5
继续
21
输入数值看是否要结束5
继续
22
输入数值看是否要结束6



i=0
while  i<1000:
    print(i)
    i+=1
    v=input('输入数值看是否要结束')
    if v=='5':
        print('继续')
    else:
        break

#执行孙旭结构下一条语句
for u in range(100):
    print(u)


0
输入数值看是否要结束5
继续
1
输入数值看是否要结束5
继续
2
输入数值看是否要结束6
0
1
2
3
...
99

直接break出while
跳到下一个for循环中


for循环中break运用
for 循环变量 in 遍历对象:
    执行代码
    if 表达式:
      break
      
于while中效果一致
跳出for循环，执行下一段代码



continie跳转语句，跳过本次循环的后续代码，继续执行下一次循环操作，也于if搭配使用
while 表达式1:
    执行代码
    if 表达式2:
        continue

i=0
s=0
while i<30:
    
    i+=1
    s+=1
    print('i is ',i)

    if s>20:
        continue
    print('s is ',s)

i is  1
s is  1
i is  2
s is  2
i is  3
s is  3
i is  4
s is  4
i is  5
s is  5
i is  6
s is  6
i is  7
s is  7
i is  8
s is  8
i is  9
s is  9
i is  10
s is  10
i is  11
s is  11
i is  12
s is  12
i is  13
s is  13
i is  14
s is  14
i is  15
s is  15
i is  16
s is  16
i is  17
s is  17
i is  18
s is  18
i is  19
s is  19
i is  20
s is  20
--------------------------------------------------------------------------------
i is  21
i is  22
i is  23
i is  24
i is  25
i is  26
i is  27
i is  28
i is  29
i is  30

s=20后
直接跳过后续s打印输出


if i%2==1:
   i+=1
   continue
位奇数时不执行if之后的程序（if 内部程序还要执行）



for循环中continue运用
for 循环变量 in 遍历对象:
    执行代码
    if 表达式:
      continue
    执行代码


空语句pass
在语法中只起到占位符作用，使语法结构完整，不报错
一般可用在if,for,while,函数的定义,类的定义中
为了保证语法结构完整，让程序不报错

#pass语句
if int(input('输入第一个数：'))>int(input('输入第二个数')):
    pass
else:
    pass

while True:
    pass
变不会报错

+++++++++++++++++++++++++++++++++++++++++++章节练习判断是否位闰年+++++++++++++++++++++++++++++++++++++++++++++++


==========================================================序列和索引======================================================================
属于序列结构的还有列表，元组，集合和字典（组合数据类型）
列表和元组位有序序列
集合于字典为无序序列

序列是一个用于存储多个值的连续空间，每个值都有对应的整数编号，称位索引
字符串也是序列
索引有正向递增索引   0~n-1
     反向递减索引    -n~-1


正向索引     
s='hello_world'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
0 h             1 e             2 l             3 l             4 o             5 _             6 w             7 o             8 r             9 l             10 d
从0开始到n-1结束

反向索引
s='hello_world'
for i in range(-len(s)-1,0):
    print(i,s[i],end='\n')
 -11 h           -10 e           -9 l            -8 l            -7 o            -6 _            -5 w            -4 o            -3 r            -2 l            -1 d

 

序列相加操作和相乘
s='hello_world1_'
y='hello_world2'
print(s+y)
hello_world1_hello_world2
序列相加

print('='*130)























==================================================================================================================================
序列相乘，则输出对应乘数个个数的序列


序列操作符/函数
x in s  若x是s的元素则为True，否则False
s not in s  若x不是s元素则为True，否则False
len()   s的元素个数（序列长度）
max()   s中元素最大值
min(s)   s中元素最小值
s.index(x) s中第一次出现元素x的位置
s.count(x) s中出现x的总次数




 #in 可以判断一个字母是否在字符串中
#在输出过程中，空格不起作用，
zhifu='hello world'
a='e'
print(a     not in     zhifu)

False

zhifu='hello world'
a='e'
print(a     in     zhifu)

True


# is 和is not  比较id是否相等
a=10
b=10
print(a is not b)

False


s='hello'
print('h' in s,'h' not in s,len(s),max(s),min(s),sep='----->')
True----->False----->5----->o----->e


s='hello'
print(s.index('l'),s.index('h'),s.count('l'),sep='----->')
2----->0----->2


s.index()若其中字符不存在s中则会报错


++++++++++++++++++++++++++++++++++++++++++++++++++++++列表
列表，指一系列按特定顺序排列的元素组成
是python中内置的可变序列
在python中使用[]定义列表，元素间用英文逗号隔开','
列表元素可以是任意的数据类型

#列表操作！列表是个大容器，可以存储n多个数，程序可以方便的对这些数进行统一处理，列表相当于C语言中的数组
#列表可以存储不同数据类型

创建方式有两种
1使用[]创建
列表名=[元素1,元素2,元素3,元素4,...,元素n,]

2使用list()函数创建
列表名=list(序列)

a=10
lst=['hello ',123,True,123.1231,a]
print(lst,type(lst),id(lst))#列表中每个元素存储的都是对应对象的id值，需要用到时候直接通过id访问

['hello ', 123, True, 123.1231, 10] <class 'list'> 3066013638080

#创建列表，1.[]   2. list（）
a=['hello world',123,123.123]
b=list('hello world',123,123.123)#两种方法等效！

print(list(range(1,100,2)),end='\n')
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

列表删除
del 列表名


lst=list('hello_world')
print(lst)
['h', 'e', 'l', 'l', 'o', '_', 'w', 'o', 'r', 'l', 'd']

序列操作方法函数在列表中均可使用如 len()   max（）等函数

lst1=list('hello_')
lis2=list('world')
print(lst1+lis2)
print(lis2*3)
print(max(lst1))
print(len(lis2))

['h', 'e', 'l', 'l', 'o', '_', 'w', 'o', 'r', 'l', 'd']
['w', 'o', 'r', 'l', 'd', 'w', 'o', 'r', 'l', 'd', 'w', 'o', 'r', 'l', 'd']
o
5

#怎么取用列表中某个指定数？ok
#怎么获取这个指定数在列表中的位置？ok
# a=['hello world',123,123.123]
print(a[0],a[1],a[2])
c=['hello ','hello','hello']#列表中数据可以重复
print(c)

#用index（）函数获取列表中元素的索引！，且当存在相同元素时，其返回的索引也是意义的，若不存在则输出valueerror，还可以在star，stop指定区间内寻找
a=['hello',12,12,4,5,6,7]
print(a.index(12))
print(a.index('hello',1,4))#在区间内寻找！

#得到索引后可以通过索引获取该元素值，可以通过正向索引{a[4]}和逆向索引a[-4]，即做到右为正，右到左为负
a=[0,1,2,3,4]
print(a[0],a[-4])#注意逆向时对应的数！！！！，可能不是想要对应的数



enumerate函数的使用语法结构（枚举）
for index,item in enumerate(lst):
     输出index和item  (序号（默认从0开始）和元素)

列表遍历操作

1 for 循环遍历
lst=list('hello_world')

for i in lst:
    print(i)
h
e
l
l
o
_
w
o
r
l
d

2根据索引
lst=list('hello_world')
for i in range(0,len(lst)):
    print(lst[i])

h
e
l
l
o
_
w
o
r
l
d

3  enumerate遍历列表

lst=list('hello_world')
for index,item in enumerate(lst):
     print(index,item)   #index为序号不是索引，可修改

0 h
1 e
2 l
3 l
4 o
5 _
6 w
7 o
8 r
9 l
10 d


lst=list('hello_world')
for index,item in enumerate(lst,start=2):
     print(index,item)   #index为序号不是索引，可修改

2 h
3 e
4 l
5 l
6 o
7 _
8 w
9 o
10 r
11 l
12 d


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
列表为可变数据类型
即，具有增加删除，改写，查询等方法（这些操作列表的内存地址均不变）

lst.append(x)    列表lst最后增加一个元素x 
lst.insert(index,x)   列表lst第index位加元素
lst.clear()           清除列表lst所有元素
lst.pop(index)        将lst第index位置元素取出并从列表中将其删除
lst.remove(x)         将lst中出现的第一个元素x删除
lst.revers(x)         将lst中的元素反转
lst.copy()            拷贝lst中所有元素并创建一个新列表
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#获取列表中多个元素，切片操作
a=[0,1,2,3,4,5,6,7,8,9]
print(a[0:4:2])#a[star:stop:step]

[0, 2]

切片结果为原列表片段的拷贝
step默认为1（未设定情况下）
step为正数；[:stop:step];;;;[star::step]>>>切片第一个元素为列表第一个元素
step为负数：[:stop:step];;[star::step]》》》切片第一个元素为列表最后一个元素

#判断元素是否在列表中！  in   not in

print('hello'in['hello',123,1234])#还可以利用列表元素进行迭代操作，for i  in []
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)
#列表元素的增减

append()  在列表末尾加一个元素
extend()  在列表末尾至少添加一个元素
insert()  在列表任意一个位置添加元素
切片操作！，任意位置至少添加一个元素

a=[0,1,2,3,4,5,6,7,8,9]
print(a)
a.append(10)
print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



a=['hellonwodl',2,3]
print(id(a))
a.append(4)
print(id(a))        #id未变
s='hello '
print(id(s))
s+='world'
print(id(s))   #id变了

#a.extend(11,12,13,14)#以列表的形式添加，而不能这样添加
a.extend([11,12,13,14,15])
print(a)

PS D:\ZUOMIAN\python> & d:/ZUOMIAN/python/.venv/Scripts/python.exe d:/ZUOMIAN/python/my_demo/day_11_18.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#print(list(a.extend(11,12,13,14)))
a.insert(1,90)#1，为位置，后面为添加数

a=[0,1,2,3,4,5,6,7,8,9]
print(a)
a.insert(2,[10,20,30,40])#这样会把这个整体当成一个字符串元素插入
print(a)
a[1:4]=[0,0,0,0]#用#号来确定区间！！1~4区间换成0
print(a)
a[1:1]=[100000,100000]#还可以指定点插入

print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, [10, 20, 30, 40], 2, 3, 4, 5, 6, 7, 8, 9]
[0, 0, 0, 0, 0, 3, 4, 5, 6, 7, 8, 9]
[0, 100000, 100000, 0, 0, 0, 0, 3, 4, 5, 6, 7, 8, 9]


#列表的删除操作！

remove()一次删除一个元素，重复元素只删除第一个，不存在元素会报错
pop()删除指定索引位置的元素，指定位置不存在会报错，不指定索引时会再末尾删除
切片，一次至少删除一个元素
clear()清空列表
del删除列表

a=[0,1,2,3,4,5,6,7,8,9]
print(a)
a.remove(9)
print(a)
a.pop(2)
print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 3, 4, 5, 6, 7, 8]



===================================================================================================================
ctrl + ?可以实现全部注释
===================================================================================================================

#注意切片会产生一个新的列表仅删除时构造一个新列表，)
a=[0,1,2,3,4,5,6,7,8,9]
print(a)
b=a[1:4]
print(b)
a.clear()
print(a)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3]
[]

del a
print(a)

会报错

a=[0,1,2,3,4,5,6,7,8,9]
print(a)
a.reverse()
print(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



t=list('hello_woerld')
print(t.pop(2))
print(t)
l
['h', 'e', 'l', 'o', '_', 'w', 'o', 'e', 'r', 'l', 'd']

#修改列表元素
a=[0,1,2,3,4,5,6,7,8,9]
#修改指定位置的一个值
a[2]=20
print(a)


[0, 1, 20, 3, 4, 5, 6, 7, 8, 9]



a=[0,1,2,3,4,5,6,7,8,9]
#sort()函数进行升序排列
lst.sort(key=None（排序的规则）方法（key=str.lower）全转换为小写后再排序,reverse=False(默认升序则位False，降序则位True))

a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)


#内置函数sorted(排序对象,key=None,reverse=False（默认升序，想降序该位True）)
b=sorted(a)#升序
会产生一个新列表对象，故要存储起来
print(b)
c=sorted(a,reverse=True)#降序
print(c)



[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


a=[0,1,2,3,4,5,6,7,8,9]
#修改指定位置的一个值
a[2]=20
print(a)

lst.sort(key=str.lower)全部转换为小写后升序

lst=list('HELLO_wOELD')
lst.sort(key=str.lower)
print(lst)
['_', 'D', 'E', 'E', 'H', 'L', 'L', 'L', 'O', 'O', 'w']

   
#编写一个G代码编译器或者解释器！！！！
#面向对象！面向过程！

#利用切片进行修改操作
a[0:2]=[10,20]
print(a)

列表生成式的语法结构
lst=[expression for item in range]

import random as r
lst=[x for x in range(13)]
print(lst)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


import random as r
lst=[x*10 for x in range(13)]
print(lst)

[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

***********************************************************
import random as r
lst=[r.randint(1,100) for x in range(13)]
print(lst)
[41, 57, 39, 27, 36, 6, 27, 84, 6, 46, 89, 31, 43]

for x in range(13)只是确定列表中元素个数，并不决定列表中元素值
r.randint(1,100) 即前面这个expression才决定列表中元素


从列表中选择符合条件的元素组成新的列表
lst=[expression for item in range if condition]


lst=[x for x in range(13) if x%2==0]
print(lst)
[0, 2, 4, 6, 8, 10, 12]
前面expression要符合x%2==0才会被放进列表中


import random as r
lst=[r.randint(1,100) for x in range(13) if r.randint(1,100)%2==0]
print(lst)
[12, 24, 8, 84, 60, 88, 89, 35]

==================================================二维列表(列表中嵌套列表)
有行和列
二维列表的遍历
for row in 二维列表:
    for item in row:
        pass


lst=[
['A','B','C'],
['E',66,77],
['F',88,99],
['G',33,55]
]

print(lst)
print()
for row in lst:#先行
    for item in row: #再列
        print(item,end='\t')

[['A', 'B', 'C'], ['E', 66, 77], ['F', 88, 99], ['G', 33, 55]]

A       B       C       E       66      77      F       88      99      G       33      55




lst=[
['A','B','C'],
['E',66,77],
['F',88,99],
['G',33,55]
]

print(lst)
print()
for x in lst:#先行
    for i in x: #再列
        print(i,end='\n')

[['A', 'B', 'C'], ['E', 66, 77], ['F', 88, 99], ['G', 33, 55]]

A
B
C
E
66
77
F
88
99
G
33
55

双for循环直接先遍历行
再遍历列



lst=[
['A','B','C'],
['E',66,77],
['F',88,99],
['G',33,55]
]
print(lst)
print()
for x in lst:#先行
    for i in x: #再列
        print(i,end='\t')
    print()

[['A', 'B', 'C'], ['E', 66, 77], ['F', 88, 99], ['G', 33, 55]]

A       B       C
E       66      77
F       88      99
G       33      55

列表生成式生成一个4行5列的二维列表


import random as r
lst=[[r.randint(1,100) for i in range(5)] for k in range(4)]

for l in lst:
    for j in l:
        print(j,end='\t')
    print()    

22      42      82      81      34
12      37      25      12      36
52      5       10      56      32
69      60      81      98      65

#核心即 for l in lst   遍历列表中的元素

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++元组++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#元组！！！！
#元组不能增删改，为不可变序列
#不可变序列，可变序列：增删该后id不会变

python中用()定义元组，元素于元素之间用英文逗号分隔
就算其中只有一个元素的时候，逗号也不能省略

元组创建方式有两种
1使用()创建元组
语法结构
元组名=(元素1,元素2,元素3,...,元素n,)


2使用内置函数tuple()创建
语法结构
元组名=tuple(序列)

删除元组
del 元组名


######################################元组只能使用索引去获取元素，和使用for循环遍历元素


t=([1,2,3,4],'hello_world',1235,6766)
print(t,type(t))
([1, 2, 3, 4], 'hello_world', 1235, 6766) <class 'tuple'>


t=tuple('hello_world')
print(t)
('h', 'e', 'l', 'l', 'o', '_', 'w', 'o', 'r', 'l', 'd')

#元组（）  三种创建方式！

1
a=(1,2,3,4,'hello world',bool(2))
print(a,type(a),id(a))

2
a=tuple((1,2,3,4,5,'helloword'))
print(a,type(a),id(a))

3
a='python',1,2,3,4,'str',bool(3)#小括号可以省略
print(a,type(a),id(a))


元组也属于序列，故关于序列的所有操作都可以操作

tuple(序列),则要为序列如字符串或者列表元组之类，前面list也是如此


t=tuple([10,20,30,40,50])
print(t,'\n')
print(10 in t)
print(10 not in t)
print(len(t))
print(max(t))

(10, 20, 30, 40, 50) 

True
False
5
50



#元组中仅包含一个元素
a=(2,)    #必须有小逗号隔开！！！
b=2,
print(a,b,type(a),type(b))

(2,) (2,) <class 'tuple'> <class 'tuple'>

#当元组中有对象为可变序列时如列表，列表中元素可以变化，因为内部元素变化不会改变其id，所以可以变，但是其他非可变序列元素就不可以变了
a=(2,3,[23,34,45],'helonwodl')
print(type(a))
print(a[0],type(a[0]),id(a[0]))
print(a[2],type(a[2]),id(a[2]))
#a[0]=20   不可变序列不可改


#但其中有列表序列或者可变序列就可以单独对其执行切片操作

a[2].append(23)
print(id(a[2]))
print()
t=a[0:3:2]
print(t)


<class 'tuple'>
2 <class 'int'> 1501939919184
[23, 34, 45] <class 'list'> 1501941685824
1501941685824

(2, [23, 34, 45, 23])


#for in 进行元组中元素的遍历
a=(2,3,[23,34,45],'helonwodl')
for item in a:
    print(item)

print()
for i in range(len(a)):
    print(i,a[i],'\t')

2 
3 
[23, 34, 45]
helonwodl

0 2
1 3
2 [23, 34, 45]
3 helonwodl 


a=(2,3,[23,34,45],'helonwodl')
for inde,itt in enumerate(a):
    print(inde,itt,'\t')

0 2 
1 3 
2 [23, 34, 45]
3 helonwodl


for inde,itt in enumerate(a,start=11):#可以规定序号从什么段开始
    print(inde,itt,'\t')

    

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++元组生成式
先生成一个序列再将序列转换为元组

故序列生成式均可用于生成元组，李彪的生成式也可以

t=(i for i in range(12))
print(t)
print(type(t))

a=tuple(t)
print(a)
print(type(a))


<generator object <genexpr> at 0x0000024F3794CCF0>
<class 'generator'>
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
<class 'tuple'>

a=(1,2,3,4,5,6,7,8,9)
print(a.__next__())
元组类型不可以用next




t=(i for i in range(12))
#生成序列对象
for i in range(12):
    print(t.__next__())

0
1
2
3
4
5
6
7
8
9
10
11 

可以是西安遍历序列对象中每一个元素
next完成后不可以转换为元组了，转换的话会为空，因next每执行一次便取出一个元素

**********************************************************************************************************************************
元组访问速度快，但是不可变，列表访问速度慢，可变
均支持切片访问
元组可以作为字典的键，但是列表不可以做为字典的键
**********************************************************************************************************************************



*************************************************************字典*****************************************************************

#字典（夫妻站）类似于夫妻关系

根据一个信息查找另一个信息的方式构成了“键值对”，表示索引用的键和对应的值构成成对的关系

key      ‘uuuu’             777     数字    [66.6.6,6]
value    7                   yyy    kie    图片     

字典中无整数索引概念，故可以通过键去索引字典中的元素
字典也为python中可变数据类型（上一个为列表）

但是字典中元素为无序的（哈希乱序）第一个添加的元素在内存中不一定在第一个位置
键于值一一对应，不可重复（值可重复，key不可），键要求不可变序列即元组那样的，整数，浮点，字符串都可以
一个key对应一个value

#字典特点

字典中所有元素均为一个key-value对，key不允许重复，value可以重复
字典中元素不是有序的不是第一个输入就在第一个位置
键必须是不可便对象，如数字字符串等，不可变，像列表等可以进行改变的就不可以左键，应为键不可变
字典中key可以更具动态进行伸缩！！？？？？？
字典会浪费较大内存，是使用空间换时间！！！！

1用{}创建字典
字典名={key1:value1,key2:value2,...,keyn:valuen}

2通过内置函数dict()创建字典
dict(key1:value1,key2:value2,...,keyn:valuen)

3通过映射函数zip(lst1,lst2)创建


a={1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置'}
b=dict(name=1,age=21) #b=dict(1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置')
print(b)#根据键值来查询值，且位置于键值有关，键值通过哈希序列变换得到位置，所有键值不能变化！！
print(a[1])#获取字典中单个元素
print(b['name'])    #方括号中为键值
print(a.get((5)),b.get('age'))  #当get的键值不存在是会返回None，可以通过此来设置退出遍历
#于是便可以用 in和  not  in 判断键值是否在字典里
print(1 in a)
#字典元素删除
del a[1]
print(a)
#字典元素新增
a[1]='hello worlf'
print(a)
#字典元素改变
a[1]='hello world222'
print(a)
a.clear()    #清空字典
print(a)

{'name': 1, 'age': 21}
hello world
1
None 21
True
{2: '可变序列', 3: '内部值可以变化,且成对存在', 4: '字典为无序，第一个放进不一定在第一个位置'}
{2: '可变序列', 3: '内部值可以变化,且成对存在', 4: '字典为无序，第一个放进不一定在第一个位置', 1: 'hello worlf'}
{2: '可变序列', 3: '内部值可以变化,且成对存在', 4: '字典为无序，第一个放进不一定在第一个位置', 1: 'hello world222'}
{}

del a #删除字典
print(a)



lst1=[10,20,30,40,50,]
lst2=['key','dog','cat','elfen','5']
a=zip(lst1,lst2)
b=zip(lst2,lst1)

print(a)
print()
print(b)

#print(a[10],a['dog'])
<zip object at 0x000002325CA06780>

<zip object at 0x000002325CA067C0>

不能看到其中内容，故要看到内容可以用list进行转换


lst1=[10,20,30,40,50,]
lst2=['key','dog','cat','elfen','5']
a=zip(lst1,lst2)
b=zip(lst2,lst1)     
print(a)
print(list(a))

<zip object at 0x000001AACED16700>
[(10, 'key'), (20, 'dog'), (30, 'cat'), (40, 'elfen'), (50, '5')]


或者直接转换为元组

lst1=[10,20,30,40,50,]
lst2=['key','dog','cat','elfen','5']
a=zip(lst1,lst2)

b=dict(a)
print(a)
print(b)
<zip object at 0x0000021510D06780>
{10: 'key', 20: 'dog', 30: 'cat', 40: 'elfen', 50: '5'}


b=dict(name=1,age=21) #b=dict(1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置')
print(b)#根据键值来查询值，且位置于键值有关，键值通过哈希序列变换得到位置，所有键值不能变化！！
print(b['name'])    #方括号中为键值
print(b[21])  #报错，因为智能通过键值去索引值，不能通过值去索引键值


键要为不可变序列，元组可以，list不行会报错
t=(10,20,30)
o={1:'777',t:'666'}
print(o)

{1: '777', (10, 20, 30): '666'}



#可变序列，则可以通过所有序列操作对其操作
a={1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置'}
print(max(a),min(a),len(a))

4 1 4

字典元素取值
d[key]或者d.get(key)


#字典元素的遍历
a={1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置'}
for item  in a:
    print(item)#item为字典中的键值

1
2
3
4    

for  i  in a:
    print(a[i],a.get(i))    #获取字典中元素值

    

hello world hello world
可变序列 可变序列
内部值可以变化,且成对存在 内部值可以变化,且成对存在
字典为无序，第一个放进不一定在第一个位置 字典为无序，第一个放进不一定在第一个位置


for x in a.values():
    print(x)                 #直接获取字典中元素值

hello world
可变序列
内部值可以变化,且成对存在
字典为无序，第一个放进不一定在第一个位置


for z in a.items():
    print(z)                  #获取字典中键值和元素对 的元组

(1, 'hello world')
(2, '可变序列')
(3, '内部值可以变化,且成对存在')
(4, '字典为无序，第一个放进不一定在第一个位置')   

for key,value in d.items:
    pass      #分别辩能力出key和value




key()获取字典中所有key
value() 获取字典中所有value
items()获取字典中key 和 value 对的元组
d.pop(key,default)  key存在获取相应value，同时删除key-value对，否则获取默认值
d.popitem()  随机从字典总获取一个key-value对，结果为元组类型，同时将该对从字典中删除
d.clear()  清空字典


a={1:'hello world',2:'可变序列',3:'内部值可以变化,且成对存在',4:'字典为无序，第一个放进不一定在第一个位置'}
print(a.keys())
print(a.values())
print(a.items())
print(list(a.items()) )       #转换之后的数据形式为元组形式


dict_keys([1, 2, 3, 4])
dict_values(['hello world', '可变序列', '内部值可以变化,且成对存在', '字典为无序，第一个放进不一定在第一个位置'])
dict_items([(1, 'hello world'), (2, '可变序列'), (3, '内部值可以变化,且成对存在'), (4, '字典为无序，第一个放进不一定在第一个位置')])
[(1, 'hello world'), (2, '可变序列'), (3, '内部值可以变化,且成对存在'), (4, '字典为无序，第一个放进不一定在第一个位置')]



#字典生成式

1
a=[1,2,3,4]
b=['hello world','key','value','items']   #若a，b元素个数不对等，就会以少的为基准进行字典生成
c=zip(a,b)
print(c)
print(list(c))
d={key:value.upper() for key,value in zip(a,b)}    #通过upper（）函数变成大写！！！
#注意这里最后面不能用变量代替   不能这样  d={key:value for key,value in c} 这样会形成空字典
print(d)
(即  d={key:value for key,value in zip(lst1,lst2)})


2
d={key:value for item in range}






#空列表
a=[]
a=list()
#空字典
b={}
b=dict()
#空元组
c=()
c=tuple()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++集合+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#集合！与字典，列表一样为可变序列，集合时没有value的字典
python中集合于数学中集合一


集合为一个无序的不重复元素序列
集合中只能存储不可变数据类型  字符串，整数，浮点，元组等数据类型，不能存储字典和列表
python中集合用{}定义


集合创建方式
1
使用{}直接创建
s={元素1,元素2,元素3,...,元素n}

a={1,2,3,4,5,5,56,6,78,8}  #集合内不能有重复元素，字典中键不能重复，集合中元素相当于字典中键
b={1:3,2:4}
print(a,type(a),b,type(b))


{1, 2, 3, 4, 5, 6, 8, 78, 56} <class 'set'> {1: 3, 2: 4} <class 'dict'>

2
使用内置函数set()创建集合
s=set(可迭代对象或者序列)

c=set(range(6))
d=set([2,3,4,5,6,7])
#set()可以将列表，元组，字典各个类型数据转换到集合中
print(d)
print(c)


{2, 3, 4, 5, 6, 7}
{0, 1, 2, 3, 4, 5}

a=set('hello eofl')
print(a)

{'l', ' ', 'o', 'h', 'e', 'f'}

#b=set(1,2,3,4,5,6)   不能直接在set（）中去列写集合内容
#定义空集合
a=set()  创建一个空集合
#不能a={}这样创建的为空字典
#in 和 not in 判断是都在集合中
print('e' in a)  #??????为什么是False
b={1,2,3,4,5,6,7}
print(20 in b)


{'l', 'f', 'h', 'e', ' ', 'o'}
False
False

还可以用max   len  min  等序列函数进行操作     

3
删除
del 集合名




#集合的数学操作
交集（A&B AB的公共部分组成一个新集合）
并集（A|B AB中所有元素组成一个集合）
差集（A-B 则A中去除于B相交那部分）
补集（A^B 去掉公共部分剩下组合为一个集合）
a={1,2,3,4,5}
b={1,2,3,5}
print(a.intersection(b))#a与b的交集
print(a&b)#也是交集表达式
print(a|b)#并集
print(a.union(b))#并集操作
print(a.difference(b))#差集???????当量集合各有一个元素不同时，的差集是怎么回事？？
#列如a={1,2,3,4}      b={1,2,3,5}只有4和5不同，但是差集之后结果会怎么样？  a-b  和b-a 为什么不同？？
print(a-b,b-a)#差集操作，但是b-a为空集？？？
print(a.symmetric_difference(b))#对称差集



{1, 2, 3, 5}
{1, 2, 3, 5}   
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{4}
{4} set()      
{4}



s.add（）一次添加一个元素
s.update（） 至少添加一个元素
s.remove（） 删除一个指定元素 若不存在抛出错误
s.discard（）删除一个指定元素，不存在不抛异常
s.pop（）删除任意一个元素
s.clear（）清空集合

a={0,1,2,3,4,5}
print(a)
a.add(10)
print(a)
a.update([20,30,40,50])
print(a)
a.update((20,30,204,90))   #这个update（）类似于set
print(a)

{0, 1, 2, 3, 4, 5}
{0, 1, 2, 3, 4, 5, 10}
{0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50}
{0, 1, 2, 3, 4, 5, 10, 204, 20, 90, 30, 40, 50}



a={0,1,2,3,4,5}
print(a)
a.add(10)
print(a)
a.update([20,30,40,50])
print(a)
a.remove(50)
print(a)
#a.remove(999)不存在会抛异常b
print(a)
a.discard(20)
print(a)
a.discard(999)   #不存在不会抛异常，正常原集合输出
print(a)
a.pop()   #删除任意元素
print(a)
a.clear() 清空集合
print(a)


{0, 1, 2, 3, 4, 5}
{0, 1, 2, 3, 4, 5, 10}
{0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50}
{0, 1, 2, 3, 4, 5, 10, 20, 30, 40}
{0, 1, 2, 3, 4, 5, 10, 20, 30, 40}
{0, 1, 2, 3, 4, 5, 10, 30, 40}
{0, 1, 2, 3, 4, 5, 10, 30, 40}
{1, 2, 3, 4, 5, 10, 30, 40}
set()



#集合关系
#是否是子集用issubset,超集用issuperset,交集用isdisjoint判断
a={1,1,2,3,4,5,6,7}
b={1,2,3,4,5,6,7}
print(a==b)
print(a!=b)
print(a is b,id(a),id(b))#id 不一样？

a={1,2,3,4}
b={1,2,3}
c={1,2,7}
d={10,}
print(b.issubset(a))#b是a的子集
print(a.issuperset(b))#a 是b的超集
print(a.isdisjoint(c))#有交集为False，无交集为True
print(c.isdisjoint(d),d)



集合的遍历操作
for item in s:
     print(itme)

     
s={1,2,3,4,5,6,'helloworld',506,(333,45,67,6)}

for i in s:
    print(i)

1
2
3
4
5
6
helloworld
(333, 45, 67, 6)
506


使用enumerate（）函数来遍历，但是集合没有索引，但是可以遍历出序号

s={1,2,3,4,5,6,'helloworld',506,(333,45,67,6)}
for idex,i in enumerate(s):
    print(idex,i,sep='------>')

0------>1
1------>2
2------>3
3------>4
4------>5
5------>6
6------>helloworld
7------>(333, 45, 67, 6)
8------>506


s={1,2,3,4,5,6,'helloworld',506,(333,45,67,6)}
for idex,i in enumerate(s,start=3):
    print(idex,i,sep='------>')


3------>1
4------>2
5------>3
6------>4
7------>5
8------>6
9------>(333, 45, 67, 6)
10------>506
11------>helloworld


集合生成式（于序列生成式一样）

s={i for i in range(15)}
print(s)

t={i for i in range(20) if i%2==1}
print(t)

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

 '''
