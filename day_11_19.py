'''
python 3.11新特性
1结构模型匹配（类似于switch结构）
match data:
      case {}:
         pass
      case []:
        pass
      case ():
        pass
      case _:  即所有前面匹配都不成功
        pass
        



data = eval(input('请输入要匹配的数据：'))
match data:
      case {'neme':ysys,'age':20}:
         print('字典')
      case [10,20,30]:
         print('列表')
      case (10,20,30):
         print('元组')
      case _:  即所有前面匹配都不成功
         print('相当于多从if中的else')

         
输入 'helloworld'则报错，使用eval（去掉引号）,没有定义
输入 "helloword"则会跳到
print('相当于if中的else')
这个


2字典合并运算符

d={'a':10,'b':20}
a={'c':30,'d':40}
y=d|a
print(y)

{'a':10,...,'d':40}




3同步迭代
match data1,data2:
   case data1,data2:
       pass

       
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
字符串及正则话表达式
bilibili    62集~84集
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#函数！

即将一段实现功能的完整代码使用函数名称进行封装，通过函数名称进行调用，达到一次编写，多次调用的目标

函数分为

内置函数：input() print() list()等

自定义函数：
def 函数名称(参数列表):
   函数体
   [return 返回值列表]（非必须，无返回值可不用）

函数调用：

函数名(参数列表)


#函数参数传递
def fun(a,b):
    c=a**b
    return c
print(fun(3,2),fun(b=2,a=3))#第一个为位置参数，第二个为关键字参数，在参数很多时可以不考虑位置，直接关键字参数进行参数设置

9 9


def fun(a,b):
    c=a**b
    return c
print(f'666的{fun(3,4)}隔断符号{fun(5,6)}')#第一个为位置参数，第二个为关键字参数，在参数很多时可以不考虑位置，直接关键字参数进行参数设置
666的81隔断符号15625

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print(f'...{}...{}..{}')可以实现字符和数字混着输出

以上a,b围殴形式参数，实际传入的3，4和5，6为实际参数

a=int(input("a:"))
b=int(input("b:"))
def fun(c,d):
    d=c*d
    c=c+d
    return c

print(fun(a,b),a,b)

a:6
b:7
48 6 7


函数的参数传递：

1位置参数
调用的参数个数和顺序必须于定义的参数个数和顺序相同
定义第一个为字符型，第二个为整数型，就必须按字符型，整数型传参


def fun(x,y):
    print('666'+x+'字符型')
    print(str(y)+'777')#默认为整数型

666tiantian字符型
19777




fun('tian')  报错

Traceback (most recent call last):
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 208, in <module>
    fun('tian')
TypeError: fun() missing 1 required positional argument: 'y'



fun(19)


Traceback (most recent call last):
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 227, in <module>
    fun(19)
TypeError: fun() missing 1 required positional argument: 'y'


fun(19,'tiantian')

Traceback (most recent call last):
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 238, in <module>
    fun(19,'tiantian')
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 219, in fun
    print('666'+x+'字符型')
TypeError: can only concatenate str (not "int") to str


参数个数，参数顺序，参数格式均不能错



2关键字参数
函数调用时，使用”形参名称=值“的方式进行传参，传递参数顺序可以与定义参数的顺序不同

#关键字传参

def fun(x,y):
    print('666'+x+'字符型')
    print(str(y)+'777')#默认为整数型
fun(x='666',y=18)
fun(y=19,x='999')


666666字符型
18777
666999字符型
19777

参数为值可以改变，但是对应参数的格式还是要遵守


fun(x=19,y=19)
Traceback (most recent call last):
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 256, in <module>
    fun(x=19,y=19)
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 251, in fun
    print('666'+x+'字符型')
TypeError: can only concatenate str (not "int") to str
只有会报错，因为参数位置对了，但是格式不对



fun(x=19,y='666')

  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 270, in <module>
    fun(x=19,y='666')
  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 262, in fun
    print('666'+x+'字符型')
TypeError: can only concatenate str (not "int") to str

还是会报错



def fun(x,y):
    print('666'+x+'字符型')
    print(str(y)+'777')#默认为整数型
fun(x='666',y=18)
fun(y=19,x='999')

可以先进行位置传参再进行关键字传参
fun('555',y=10)

666666字符型
18777
666999字符型
19777
666555字符型
10777


但是不可以先关键字传参，在位置传参

fun(x='666',18)

  File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 299
    fun(x='666',18)
                  ^
SyntaxError: positional argument follows keyword argument


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
规则是位置参数在前，关键参数在后的原则
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


3默认值参数
函数定义值直接对形式参数进行赋值，第哦啊用时如果该参数不变，则用默认的值，该参数传参，则用新参数值


#在函数参数定义时，设默认值参数，当输入参数不一致时才修改参数
def fun(a,b=20):
    return a,b
print(fun(90))  #按顺序穿给第一个参数
print(fun(90,30))  #按顺序第一个第二个参数都传
print(fun(10))#只是上次改变时会改变若不改变还是默认


但是传参是按位置参数进行传的，故要符合格式，不要第一个位置为字符串型，但是传入了整数型

(90, 20)
(90, 30)
(10, 20)


def fun(a,b=20):
   pass



def fun(a=20,b):
   pass
   
当位置参数和关键字参数同时存在时，要位置参数在前，关键字参数在后（或者默认值参数在后）



4可变参数
可变参数分为个数可变的位置参数，和个数可变的关键字参数两种
个数可变的位置参数是在参数前加一颗星（*para），para为形式参数的名称，函数调用时可接受任意个数的实际参数，并放到一个元组中
个数可变的关键字参数是在参数前加两个星（**para），在函数调用时可接受任意多个"参数=值"形式的参数，并方到一个字典中




#函数参数定义，个数可变的位置参数，个数可变的关键字参数
#传入参数输入会被转换为元组格式
def fun(*a):#里面参数只能定义一个
    print(a,type(a))
    for i in a:
      print(i)
    return a
fun(1,2,3,4,5,6,7)#个数可以变

(1, 2, 3, 4, 5, 6, 7) <class 'tuple'>
1
2
3
4
5
6
7




#且输入会被转换为元组格式
def fun(*a):#里面参数只能定义一个
    print(a,type(a))
    for i in a:
      print(i)
    return a
fun(1,2,3,4,5,6,7)#个数可以变
fun([1,2,3,4,5])  #虽然传的时列表但是相当于只传一个元素


(1, 2, 3, 4, 5, 6, 7) <class 'tuple'>
1
2
3
4
5
6
7
([1, 2, 3, 4, 5],) <class 'tuple'>
[1, 2, 3, 4, 5]





def fun(*a):#里面参数只能定义一个
    print(a,type(a))
    for i in a:
      print(i)
    return a

fun([1,2,3,4,5])  #虽然传的时列表但是相当于只传一个元素
fun(*[1,2,3,4,5])  #对此列表进行解包

[1, 2, 3, 4, 5]
(1, 2, 3, 4, 5) <class 'tuple'>
1
2
3
4
5




想将传入列表中每一个元素都当成传入参数
#在调用时参数前加一个颗星*，此时会将列表进行解包
fun(*[1,2,3,4,5])

def fun(**a):#里面参数只能定义一个    这个有什么用？？
    print(a)




def fun(**a):#传入参数被整理成一个字典进行存储
    print(a,type(a))
    #对字典进行遍历
    for x,y in a.items():
      print(x,y)

#调用，则为个数可变的关键字参数
fun(y='777',name=99,t=00,hight=190)


{'y': '777', 'name': 99, 't': 0, 'hight': 190} <class 'dict'>
y 777
name 99
t 0
hight 190

fun(a=[1,2,3,4,5],b=34,c=45)


也可以对字典进行解包

def fun(**a):#传入参数被整理成一个字典进行存储
    print(a,type(a))
    #对字典进行遍历
    for x,y in a.items():
      print(x,y)
a={'nema':66,'high':190,'6':90}


字典中key必须为字符串形式
#a={'nema':66,'high':190,6:90}
# Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_19.py", line 456, in <module>
#     fun(**a)
# TypeError: keywords must be strings

fun(**a)

{'nema': 66, 'high': 190, '6': 90} <class 'dict'>
nema 66
high 190
6 90


在一个函数定义过程中，既有个数可变的位置形参，也有关键字可变的形参，！！！个数可变的位置形参必须在关键字形参之前！


def fun(*a,**b):#这样才可行
    print(a,b)
#def fun(**a,*b):这样不行
 #   print(0)

#将序列中每个元素转换为位置实参    *    将字典中每个键值转换为关键字实参**
def fun (a,b,c,d):
    print(a,b,c,d)
fun(1,2,3,4)
a=[10,20,30,40,]#这样就可以直接将列表中参数转换为函数中实际参数
fun(*a)
b={'a':2,'b':3,'c':5,'d':9}
fun(**b)#两个*将字典中值传入函数。。。一个*将字典中键值传入函数


++++++++++++++++++++++++++++++++++++++++++++++++++++++其他+++++++++++++++++++++++++++++++++++++++++++++



#对于可变对象在函数调用后是否会改变？？
def fun(x,y):
    print(x)
    print(y)
    x=100
    y.append(200)
    print(x)
    print(y)

n=10
m=[1,2,3,4]
print(n)
print(m)
print('--------------------------')
fun(n,m)
print('*****************************************')
print(n)#输出n为10 没变，则对不可变元素经过函数调用后虽然函数内部会变化，但是函数外的不会变，无影响
print(m)#可变的变量在经过函数变化后会变化！列表，字典！


10
[1, 2, 3, 4]
--------------------------
10
[1, 2, 3, 4]
100
[1, 2, 3, 4, 200]
*****************************************
10
[1, 2, 3, 4, 200]



#函数进行参数传递过程中，如果不可变对象，在函数体内的修改不会影响实参的值，可变对象则会影响到哦实际参数！
#当函数需要返回多个参数时，返回结果为元组形式！
def fun(s):
    a=0
    b=0
    a+=5+s
    b+=s
    return a,b
print(fun(5))#多个参数值返回的时元组形式


(10, 5)

'''


