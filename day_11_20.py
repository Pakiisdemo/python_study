'''
*************************************************************函数返回值****************************************************************
函数运行结果，需要在其他函数中使用，那么这个函数就应该被定义为带返回值的函数
函数运行结果使用return关键字进行回传
return可以出现在函数中的任意一个位置，用于结束函数
返回值可以是一个值或多个值，如果返回值是多个，结果是一个元组类型


#无返回值函数。返回值为None
def fun(a,b):
    print(a+b)


print(fun(1,2)
      
)


3
None


#有返回值函数
def sum(a,b):
    return a+b
print(sum(3,4))



7


#有返回值函数
def sum(a,b):
    return a+b
print(sum(sum(5,6),4))#可以将有返回值的函数作为一个值使用

15


#多个返回值

def summ(num):
    s=0
    j=0
    k=0
    for i in range(50):
        s+=i
    for i in range(30):
        j+=i
    for i in range(10):
        k*=i
    return s,j,k
   
print(summ(99))

(1225, 435, 0)

多个返回值为一个元组

#解包赋值

def summ(num):
    s=0
    j=0
    k=0
    for i in range(50):
        s+=i
    for i in range(30):
        j+=i
    for i in range(10):
        k*=i
    return s,j,k
a,b,c=summ(99)
print(a,b,c,summ(66),type(summ(55)))

1225 435 0 (1225, 435, 0) <class 'tuple'>




*************************************************************变量作用域****************************************************************
变量作用域指变量起作用的范围，有作用域大小可分为   局部变量和全局变量

局部变量，在函数定义处的参数和函数内部定义的变量
作用范围：仅在函数内部，函数执行结束，局部变量的生命周期也结束


def summ(num):
    s=0
    j=0
    k=0
    for i in range(50):
        s+=i
    for i in range(30):
        j+=i
    for i in range(10):
        k*=i
    return s,j,k

s,j,k均为局部变量



全局变量，在函数外定义的变量或函数内部使用global关键字修饰的变量
作用范围：整个程序，程序运行结束，全局变量生命周期才结束

a=10
b=20
c=40

def summ(num):
    a=0  #当局部变量与全局变量名称相同时局部变量优先参与运算，即先用其在函数内部赋的值
    b=0
    k=0
    for i in range(50):
        a+=i
    for i in range(30):
        b+=i
    for i in range(10):
        k*=i
    return a,b,k
print(a,b,c)
print(a,b,c,summ(68))

10 20 40
10 20 40 (1225, 435, 0)

全局变量未变。且可以在函数中进行赋值操作，但是最后还是会回归最开始的全局赋值


a=10
b=20
c=40

def summ(num):
    a=0  #当局部变量与全局变量名称相同时局部变量优先参与运算，即先用其在函数内部赋的值
    b=0
    global k
    k=200
    for i in range(50):
        a+=i
    for i in range(30):
        b+=i
    for i in range(10):
        k*=i
    return a,b,k
#print(a,b,c,k)  报错，应为函数未使用，k还未定义

print(a,b,c,summ(68),k)   #而且要先调用summ（）函数，在调用K
不然会报错说k未定义

10 20 40 (1225, 435, 0) 0

k的值会变


def fun(x,y):
    global s
    s=100
    return s+x+y
print(fun(3,4),type(fun(5,6)),s)

107 <class 'int'> 100


匿名函数lambda：指没有名字的函数，这种函数只能使用一次，一般在函数的函数体只有一句代码且只有一个返回值
时可以使用匿名函数来简化

语法结构：
result=lambda 参数列表:表达式


def fun(x,y):
    s=100
    return s+x+y

print(fun(9,90))
d=100
k=lambda x,y:x+y+d
print(k(9,90))   #调用匿名函数方法

199
199


#列表取值也可以匿名
a=[10,20,30,40]

for i in range(len(a)):
    s=lambda x:x[i]
    #print(s[i])  #[]是错的
    print(s(a))   #传值为列表型

10
20
30
40

排序时使用
94集末尾，python子木


递归

在一个函数体内部调用该函数本身，该函数就是递归函数
一个完整的递归操作由两部分组成，一部分递归调用，一部分递归终止条件，一般可使用if-else结构来判断递归的调用和递归的终止

def fun(x):
    if x==1:
        return 1  (下一次调用的函数值)（相当于fun(n-1)）    
    else:
       return  x*fun(x-1)     当最后时是   2*fun(1)   即2*1 
print(fun(5))

120


python中常用的内置函数   数据类型转换函数

bool()
str()
int()
float()
list(序列)
tuple(序列)
set(序列)

a=[1,2,3,4]
str(a)
也可以将列表转换为str类型



常用数学函数

abs(x)取绝对值
divmod(x,y) 取x和y的商和余数
max(lst) 取序列的最大值
min(lst)取序列的最小值
sum(lst) 求和

print(sum([1,2,3,4,5,6]))
21

pow(x,y)获取x的y次幂
round(x,d)对x进行保留d位小数，结果四舍五入

常用的迭代器操作函数

sorted()           对可迭代对象进行排序
reversed()         反转序列生成新的迭代器对象，即序列
zip(lst1,lst2)     将lst1和lst2打包为元组并返回一个可迭代的zip对象  即字典
enumerate()        根据迭代对象创建enumerate对象（包含序列号和对应值）
all()              判断迭代对象中所有元素的bool（）值是否为True
any()              判断迭代对象中所有元素的bool（）值是否为False
next()             获取迭代器的下一个迭代器对象
filter(function,iter)  通过特定条件过滤序列并返回一个迭代器对象
map(function,iter)     通过函数function对迭代对象iter操作，并返回一个迭代器对象

def fun(x):
    return x%2==1
s=filter(fun,range(20))#将range（20）中每个元素都执行一次fun函数操作

print(s)
print(list(s))

<filter object at 0x000001B9D5AF2E80>
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


new=['helo','uuu','kkk']
def fun(x):
    return x.upper()

s=map(fun,new)
print(s)
print(list(s))


<map object at 0x000002C926B22E80>
['HELO', 'UUU', 'KKK']


其他常用的函数

format(value,format_spec)  将value以format_spec格式进行显示
len(s)    获取s的长度或者元素个数
id(obj)   获取对象的内存地址
type(x)   获取x的数据类型
eval(s)   执行x这个字符串所表示的python代码  即去掉左右单引号




print(format(3.14,'30'))#将对象转化未30个字符的数据
print(format('hellow','30'))


                          3.14    数字右对齐
hellow                            字符左对齐


print(format('hello','*<20'))
print(format('heloo','$<20'))
hello***************
heloo$$$$$$$$$$$$$$$
直接填充空额部分


print(format('hellow','#>30'))
print(format('内置函数','#^130'))

########################hellow
###############################################################内置函数###############################################################
右对齐填充
和中间对齐填充


print(format(3.1415925,'.2f'))
print(format(20,'b'),format(20,'o'),format(20,'x'))
3.14
10100 24 14
保留几位有效数字
转换未二进制八进制十六进制格式

###############################################################面向对象###############################################################

面向过程和面向对象
面向过程代表 C语言
功能上的封装，编写函数就是实现功能上的封装
即面向过程的思想


面向对象代表python和java
属性和行为上的封装即类和对象

把东西归类，将n多个对象抽除'像'的属性和行为，从而总结归纳未一种类别

类别中的一个具体对象，对象中有属性和行为

python一切皆为对象
字符串对象  ‘hello’  ，整数对象1，2，3，4

type可查看对象类型

a='666'
b='hello'
c=99
d=9.32

print(type(a),type(b),type(c),type(d))


<class 'str'> <class 'str'> <class 'int'> <class 'float'>
全为class   一切皆对象



#类的创建！
自定义数据类型的语法结构为
class 类名():  类名首字母大写，后面（）可写可不写
    pass


类为图纸，一个抽象模板，只有创建对象后才可以使用
class Person():
    pass
class Cat():
    pass
class Dog:
    pass



class Student:#相当于一个模板，只有创建对象后才可以使用
    native_pace='东北'#直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name=name#self.name   #为实例属性后面的name可以自己定义，一般是与后面赋值的变量名相同
        self.age=age
    def set(self):                 #类中定义的为方法！实例方法
        print('实例方法')
 

创建对象的语法格式为
对象名=类名()
类名赋值给一个变量存储

变量即对象名

#创建一个Person类
class Person:
    pass
#创建一个Person类型的对象
per=Person()

print(type(per))

<class '__main__.Person'>


'''

'''
        
类的组成  #类的组成，类属性，实例方法，静态方法，类方法
##############类属性     直接定义在类中，方法外的变量

##############实例属性   定义在__init__方法中，使用self打点的变量

##############实例方法   定义在类中的函数，而且自带参数self

#实例方法 
    def set(self):#类中定义的为方法！实例方法
        print('实例方法')

静态方法   使用装饰器@staticmethod修饰的方法

#静态方法
    @staticmethod
    def method():
        print('staticmethod')


################类方法     使用装饰器@classmethod修饰的方法

#类方法
    @classmethod
    def fun(cls):
        print('classmethod')

# def set(a):
      #  print('hello world')
    
print(Student,id(Student),type(Student))


**************************************************************类的标准模板**************************************************************

class Student:
    #类属性；定义在类中方法外的变量
    school='66刚开始'  #就是一个变量，只是它定义的位置在类里面，所以其名称就变量
    #实例属性：先有个方法，方法名称叫初始化方法
    # def __init__(self):#方法，则可以传参
    #     pass
    def __init__(self,name,age):#name,age为方法的参数，为局部变量,故其使用范围仅限于当前方法__init__
        #为了在方法外也使用到这几个变量，则可以用实例属性来操着
        self.xm=name   #=左侧是实例属性，name是局部变量，将局部变量值name赋值给实例属性self.xm
        self.age=age #实例属性名称和局部变量名称可以相同
    
    #类中定义的为方法！实例方法
    #定义在类中的函数即为方法，
    def set(self):
        print(f'名字叫：{self.xm},今年：{self.age}')

    #静态方法，也为方法只是装饰器不同   静态方法不带self,小括号中参数写就有参数，不写就没有参数
    @staticmethod
    def sm():
        print('静态方法，且方法中不可以调用实例属性和实例方法,会报错')
    #类方法,会自带cls   即class的简写
    @classmethod
    def cm(cls):
        print('类方法，其中也不能调用实例属性和实例方法')        

#类定义好了，但是还不能用，想要用必须创建一个对象

#创建类对象

kk=Student('KK',18)#__init__方法中有两个形参，name和age,self不用管，自带参数，无需手动传入
#实例属性,使用对象名打点使用
print(kk.xm,kk.age)

# KK 18

#类属性，直接使用类名取打点调用
print(Student.school)

# 66刚开始

#实例方法,与实例有关的都是对象名打点调用
kk.set()

# 名字叫：KK,今年：18


#类方法，直接使用类名进行打点调用
Student.cm()
# 类方法，其中也不能调用实例属性和实例方法


#静态方法，直接类名进行打点调用
Student.sm()

# 静态方法，且方法中不可以调用实例属性和实例方法,会报错



# 与实例有关则用对象名打点取调用，与其他用类名取打点调用


**************************************************************类的标准模板**************************************************************


#类当中的对象的创建
class Student:#相当于一个模板
    native_pace='东北'#直接写在类里面的变量称为类属性,被该类中所有对象共享，相当于一个全局变量
    name1='沈阳'
    def __init__(self,name,age):
        self.name=name#self.name为实例属性后面的name可以自己定义，一般是与后面赋值的变量名相同
        self.age=age
#实例方法
    def set(self):#类中定义的为方法！实例方法
        print('实例方法')
#静态方法
    @staticmethod
    def method():#
        print('staticmethod')
#类方法
    @classmethod
    def fun(cls):#cls表明调用时候不需要传入参数
        print('classmethod')

stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)#输出了它的内存地址
print(stu1.name,stu1.age)
stu1.fun()
stu1.set()
stu1.method()
#类似上述方法的还有
Student.set(stu1)#只有在括号里面是self的才可以
#Student.name1='沈阳2'#修改总类，会导致子类中对应属性改变
stu1.name1='沈阳2'#系应该子类则不会影响主类
print(Student.native_pace)
print(Student.name1
      ,stu1.name1)
stu2=Student('1',20)
print(stu2.name1)


**************************************************************使用模板创建多个对象**************************************************************

class Student:
    #类属性；定义在类中方法外的变量
    school='66刚开始'  #就是一个变量，只是它定义的位置在类里面，所以其名称就变量
    #实例属性：先有个方法，方法名称叫初始化方法
    # def __init__(self):#方法，则可以传参
    #     pass
    def __init__(self,name,age):#name,age为方法的参数，为局部变量,故其使用范围仅限于当前方法__init__
        #为了在方法外也使用到这几个变量，则可以用实例属性来操着
        self.xm=name   #=左侧是实例属性，name是局部变量，将局部变量值name赋值给实例属性self.xm
        self.age=age #实例属性名称和局部变量名称可以相同
    
    #类中定义的为方法！实例方法
    #定义在类中的函数即为方法，
    def set(self):
        print(f'名字叫：{self.xm},今年：{self.age}')

    #静态方法，也为方法只是装饰器不同   静态方法不带self,小括号中参数写就有参数，不写就没有参数
    @staticmethod
    def sm():
        print('静态方法，且方法中不可以调用实例属性和实例方法,会报错')
    #类方法,会自带cls   即class的简写
    @classmethod
    def cm(cls):
        print('类方法，其中也不能调用实例属性和实例方法')    

tt=Student('tt',18)
kk=Student('KK',19)
oo=Student('oo',20)
uu=Student('uu',21)

# print(type(tt))
# print(type(kk))
# print(type(oo))
# print(type(uu))

# <class '__main__.Student'>
# <class '__main__.Student'>
# <class '__main__.Student'>
# <class '__main__.Student'>

#给类属性赋值
Student.school='666'

#将其存入列表中
# lst=[tt,kk,oo,uu]#列表中存储了四个元素，都是Student类型的对象

# for i in lst:
#     print(type(i),i)
#     #既然是对象则可以进行所有对象操作
#     i.set()

# <class '__main__.Student'> <__main__.Student object at 0x0000026626F18F70>
# 名字叫：tt,今年：18
# <class '__main__.Student'> <__main__.Student object at 0x0000026626F18EE0>
# 名字叫：KK,今年：19
# <class '__main__.Student'> <__main__.Student object at 0x0000026626F18D60>
# 名字叫：oo,今年：20
# <class '__main__.Student'> <__main__.Student object at 0x0000026626F18D00>
# 名字叫：uu,今年：21



#动态绑定属性和方法
每个对象的属性名称相同，但属性值不同




class Student:
    name1='张三'
    def __init__(self,name,age):
        self.name=name#这里是self而不是Student
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')


stu1=Student('张三',21)#student类的实例对象
stu2=Student('李四',22)
stu1.eat()
stu2.eat()
print('------------------------------------')

# 可以为某个对象绑定独有的属性或方法

# 动态绑定一个实例属性
stu2.gender='女'#动态加上一个gender    
Student.gender2='zhon'#在总类上添加一个属性
print(stu1.name,stu1.age,stu1.name1,stu1.gender2)
print(stu2.name,stu2.age,stu2.gender,stu2.gender2)

# 张三在吃饭
# 李四在吃饭
# ------------------------------------
# 张三 21 张三 zhon
# 李四 22 女 zhon




#动态绑定方法
class Student:
    name1='张三'
    def __init__(self,name,age):
        self.name=name#这里是self而不是Student
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')
stu1=Student('张三',21)#student类的实例对象
stu2=Student('李四',22)

#先定义一个函数
def f(x):
    print('定义新方法')
    print(x)
stu1.zijixiedefangfamin=f  #自己写的方法名，加小括号是调用，不加是赋值
stu1.zijixiedefangfamin(3)   


# 定义新方法
# 3

stu1.f(3)
#没有为stu1定义动态方法，故搜寻不到
# #Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_20.py", line 687, in <module>
#     stu1.f(3)
# AttributeError: 'Student' object has no attribute 'f'
'''
