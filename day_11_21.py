#封装！
'''

面向对象的三大特征：
封装：提高程序安全性；
将数据属性和方法包装到类对象中，在方法内部对属性进行操作，在类对象外部第哦啊用方法，隔离了复杂度，无需关系具体实现细节
隐藏内部细节，对外提供操作方式
pytho中没有专门的修饰符用于属性私有，如果不希望在类外部访问该属性，则前面使用两个__
隐藏内部细节，对外提供访问属性和方法的访问方式

python中没有明确的权限访问修饰符
对权限的访问控制，提供对属性和方法      添加下划线来实现，有单下划线，双下划线，及首位双下划线

单下划线开头：以单下划线开头的属性或方法表示protected受保护的成员，这类成员被视为仅供内部使用，允许类本身和子类进行访问，
但实际上可以被外部代码访问（强行访问可以访问）

双下划线开头：表示private私有的成员，这类成员只允许定义该属性或方法的类本身访问

首位双下划线：一般表示特殊方法（如初始化方法）

继承：提高代码复用性                              （类似于关键字参数？）
函数调用时使用'形参名称=值'的方法进行传参，传递参数顺序可以与定义时参数顺序不同

多态：提高程序扩展性，和可维护性                   （类似与默认参数？？）
在函数定义时直接对形式参数进行赋值，在调用时如果该参数不传值，则使用默认值，传值则使用新值



##############################################################权限访问实操##############################################################


class Student:

    school='66刚开始'  

    def __init__(self,name,age,gender):    #name,age为方法的参数，为局部变量,故其使用范围仅限于当前方法__init__

        self._name=name             #self._name 受保护变量，只能本类或者其子类使用
        self.__age=age              #self.__age 私有的，只能类本身取使用
        self.gender=gender          #普通实例属性,类内部外部和子类都可以使用

    def _set(self):                 #受保护方法,子类和本身可以访问
        print(f'名字叫：{self._name},今年：{self.gender}')
    
    def __fun(self):
        print('私有的，只有定义的类，可以访问')

    def fun2(self):
        self._set()              #可以访问受保护的方法
        self.__fun()             #可以访问私有的方法
        print('普通的实例方法')
 
    @staticmethod
    def sm():
        print('静态方法，且方法中不可以调用实例属性和实例方法,会报错')

    @classmethod
    def cm(cls):
        print('类方法，其中也不能调用实例属性和实例方法')    


stu=Student('KK',22,'women')

print(f'受保护的变量可以通过类和其子类输出{stu._name}')

# 受保护的变量可以通过类和其子类输出KK
#print(stu.__age)

# Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_21.py", line 68, in <module>
#     print(stu.__age)
# AttributeError: 'Student' object has no attribute '__age'

#出了类的范围就不可以使用了
stu._set()

# 受保护的变量可以通过类和其子类输出KK
# 名字叫：KK,今年：women
# 受保护方法子类可以调用

stu.__fun()

# 受保护的变量可以通过类和其子类输出KK
# 名字叫：KK,今年：women
# Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_21.py", line 82, in <module>
#     stu.__fun()
# AttributeError: 'Student' object has no attribute '__fun'

# 私有的不可以访问


class Car:
    def __init__(self,brand,value):
        self.brand=brand
        self.__value=value
    def star(self):
        print('汽车启动',self.brand,self.__value)
car=Car('JEEP',20)
car.star()
print(dir(car))#通过dir函数可以将类多项中的所有属性和方法列出来
print(car.brand,car._Car__value)#可以提高_+类名+__隐藏属性名    来访问隐藏属性



#######################################################想要访问则需要

class Student:

    school='66刚开始'  

    def __init__(self,name,age,gender):    #name,age为方法的参数，为局部变量,故其使用范围仅限于当前方法__init__

        self._name=name             #self._name 受保护变量，只能本类或者其子类使用
        self.__age=age              #self.__age 私有的，只能类本身取使用
        self.gender=gender          #普通实例属性,类内部外部和子类都可以使用

    def _set(self):                 #受保护方法,子类和本身可以访问
        print(f'名字叫：{self._name},今年：{self.gender}')
    
    def __fun(self):
        print('私有的，只有定义的类，可以访问')

    def fun2(self):
        self._set()              #可以访问受保护的方法
        self.__fun()             #可以访问私有的方法
        print('普通的实例方法')
 
    @staticmethod
    def sm():
        print('静态方法，且方法中不可以调用实例属性和实例方法,会报错')

    @classmethod
    def cm(cls):
        print('类方法，其中也不能调用实例属性和实例方法')   

stu=Student('KK',19,'women')

###########################################################################想要访问私有变量
print(stu._Student__fun)
stu._Student__fun()
# <bound method Student.__fun of <__main__.Student object at 0x00000298ED897BB0>>
# 私有的，只有定义的类，可以访问

#可以使用dir取查看所有属性和类
print(dir(stu))

['_Student__age', '_Student__fun', '__class__', '__delattr__', '__dict__', '__dir__', 
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 '__weakref__', '_name', '_set', 'cm', 'fun2', 'gender', 'school', 'sm']

#不建议这样访问私有属性


在编写程序时可以使用装饰器，@property将一个方法转化为属性取使用

只有就是你访问不能修改，若想想修改，还需要设置一个setter这样的一个方法擦可以取需修改属性值




class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        #私有属性不建议用_Student__age取强制访问
        #想要访问可以通过property修饰器
    @property
    def age(self):
        return self.__age
    #想将age属性设置为可写属性
    #@property.setter    #这样会报错
    @age.setter
    def age(self,value):
        self.__age=value
    
stu=Student('KK',22)
print(stu.name,stu.age)#age虽然为方法，但是有property修饰后，就不需要加（）可以实现访问

#此时方法当属性使用
# KK 22

# 此时只能查看值，取不能修改值
# 尝试修改__age

# 直接赋值
#stu.age=18

# KK 22
# Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_21.py", line 183, in <module>
#     stu.age=18
# AttributeError: can't set attribute 'age'


#会报错

#@property.seter
stu.age=19
print(stu.age)

# Traceback (most recent call last):
#   File "d:\ZUOMIAN\python\my_demo\day_11_21.py", line 164, in <module>
#     class Student:
#   File "d:\ZUOMIAN\python\my_demo\day_11_21.py", line 175, in Student
#     def age(self,value):
# TypeError: descriptor 'setter' for 'property' objects doesn't apply to a 'function' object

#会报错

# 那边不要使用property，应该使用属性名称

#应设置为@age.setter  才对
# KK 22
# 19

################################################################继承################################################################

#继承
#如果一个类没有继承任何类，则默认继承object
#python支持多继承

在python中一个子类可以继承N多个父类
一个父类也可以拥有N多个子类


继承的语法结构
class 类名(父类1,...,父类N):
     pass
     


#单继承
class Car(object):
    a=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setup(self):
        print('setup')

car=Car('奔驰',20)
car.setup()

#正常使用类中方法

print(car.a,car.name,car.age)


class littalcar(Car):
    def __init__(self,name,age,score):
        super().__init__(name,age)#####主要是supper（）来继承父类的属性
        self.score=score
cc=littalcar('jeck',20,98)
cc.setup()#继承了父类的一切，包括属性和方法
print(cc.age,cc.name,cc.a,cc.score)



# setup
# 10 奔驰 20
# setup
# 20 jeck 10 98



#多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):#这样为多继承！
    pass

    

class FatherA():
    def __init__(self,name):
        self.name=name
    
    def showA(self):
        print('父类A中的方法')

class FatherB():
    def __init__(self,age):
        self.age=age
    
    def showB(self):
        print('父类B中的方法')


# 多继承

class Son(FatherA,FatherB):
    def __init__(self, name,age,gender):
        #需要调用两个父类的初始化方法
        #super().__init__(name)   多个父类，此时supper不知道调用哪个父类初始化方法
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
        self.gender=gender

son=Son('name',18,'66')
son.showA()  #父类A中定义方法
son.showB()  #父类B中定义方法


# 父类A中的方法
# 父类B中的方法



###############################################################方法重写###############################################################
#方法重写
#当子类对父类某个属性不满意时，可以在子类中对其进行重新编写
#子类从写后的方法可以通过supper().xxx()调用父类中被重写的方法

子类继承了父类就拥有了父类中公有的成员和受保护成员，
父类方法并不完全适合子类的需求，此时子类可重写父类的方法
子类在重写父类方法时，要求方法名称必须与父类方法的名称相同，在子类重写后的方法中，可以通过super().xx()调用父类中的方法

每个子类都可以重写方法

class Car(object):
    a=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setup(self):
        print('setup')

car=Car('666',8)
car.setup()


# setup


class littalcar(Car):
    def __init__(self,name,age,score):
        super().__init__(name,age)#####主要是supper（）来继承父类的属性
        self.score=score
    def setup(self):
        print('重写1')#这里只输出从写，如果想输出父类的则：  父类已经输出'setup'。此时从写可以不用管，在从写一个'重写'
        super().setup()#这里将父类中的也进行运行（即输出'setup'）若不想输出是不是可以不写这一句????

li=littalcar('777',18,99)
li.setup()


# 重写1
# setup

class littalcar2(Car):
    def __init__(self,name,age,score):
        super().__init__(name,age)#####主要是supper（）来继承父类的属性
        self.score=score
    def setup(self):
        print('重写2')#这里只输出从写，如果想输出父类的则：  父类已经输出'setup'。此时从写可以不用管，在从写一个'重写'
        super().setup()#这里将父类中的也进行运行（即输出'setup'）若不想输出是不是可以不写这一句????

lii=littalcar2('88',19,100)
lii.setup()





# 重写2
# setup



class littalcar2(Car):
    def __init__(self,name,age,score):
        super().__init__(name,age)#####主要是supper（）来继承父类的属性
        self.score=score
    def setup(self):
        print('重写2')#这里只输出从写，如果想输出父类的则：  父类已经输出'setup'。此时从写可以不用管，在从写一个'重写'
        #super().setup()#这里将父类中的也进行运行（即输出'setup'）若不想输出是不是可以不写这一句????

lii=littalcar2('88',19,100)
lii.setup()


# 重写2
# 不想要父类的方法，则不写super().setup()即可



################################################################多态################################################################


#多态

指'多种形态'，即不知道一个变量所引用的对象到底时什么类型，任然可以通过这个变量调用对象的方法
在程序运行过程中根据变量所引用的对象数据类型，动态决定调用哪个对象中的方法
python语言中的多态，根本不关心对象的数据类型，也不关系类之间是否存在继承关系，只关心对象的行为（方法），只要不同类中有同名的方法即可实现多态

#即便不知道一个变量引用的对象到底是什么类型，任然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法


class Animal(object):
    def eat(self):
        print('动物吃')
class Dog(Animal):
    def eat(self):
        print('狗吃')
class Cat(Animal):
    def eat(self):
        print('猫吃')


class Person(object):
    def eat(self):
        print('人吃')

#三个类中都有同名方法 eat

#编写函数
def f(obj):  #obj为函数形参,不用关其什么数据类型
    obj.eat()  #通过obj(对象)调用eat方法

an=Animal()
f(an)  #直接传入类名或者对象名都可以
f(Animal())
f(Dog())
f(Cat())
f(Person())


# 动物吃
# 动物吃
# 狗吃
# 猫吃
# 人吃

# 即定义一个函数,这个函数实现类中的一个名称的方法,只要可以打包多个类,不用再写   对象.方法(),只要再函数中传入类名即可

一个方法函数直接调用这个对象,只要这个对象有这个方法即可(不关心对象数据类型,也不关心从哪继承,只关心,是否有这个名字的方法)



如果一个类没有继承任何类,则其默认继承object类
#object类时所有类的直接或间接的父类
#因此所有类都有object类的属性和方法。
#内置函数dir()可以查看指定对象所有属性

#object类中特殊的方法
_new_()   由系统调用,用于创建对象      自动调用 
_init_()  创建对象时手动调用,用于初始化对象属性值       自动调用
_str_()   对象的描述,返回值为str类型,默认输出对象的内存地址


先执行_new_()方法取创建对象,开辟内存空间,创建完成后,再由_init_()方法去给实例属性赋值

#object有一个_str_()方法，用于返回到一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对_str_()进行重写



class Person():
    def __init__(self):
        pass
per=Person()
print(dir(per))


['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
   '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
     '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
     '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# 上面非自己定义的属性和方法均时由object类中继承来的

print(per)   #自动调用了__str__方法


<__main__.Person object at 0x0000021D68DBA980>


_str_返回为内存地址


#__str__方法从写


class Person():
    def __init__(self):
        pass
per=Person()


#重写前
print(per)   #自动调用了__str__方法


# <__main__.Person object at 0x0000021D68DBA980>



class Person():
    def __init__(self):
        pass
    def __str__(self):
        return "重写str方法"
per=Person()
print(per)

#也可手动调用
print(per.__str__())

# 重写str方法     输出不在时内存地址,该成重写后的字符串了



class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字为{},今年{}岁'.format(self.name,self.age)###这种格式来写！！！好像只能用在return中

stu=Student('3',23)
print(dir(stu))
print(stu)

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
我的名字为3,今年23岁


'''


'''
首尾双下划线为特殊方法

#特殊方法
一下均为首尾双下划线
+        __add__()                               加法运算
-        __sub__()                               减法
<,<=,==  __lt__(), __le__(), __eq__()                比较
>,>=,!=  __gt__(), __ge__(), __ne__()                比较
*,/      __mul__(), __truediv__()                  乘法,非整除运算
%,//     __mod__(), __floordiv__()                 执行取余运算,整数运算
**       __pow__()                               执行幂运算



a=20
b=100
c=a+b
d=a.__add__(b)
print(dir(a))
print(a+b)
print(c)
print(d)


['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
  '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
    '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
      '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', 
      '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
        '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', 
        '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', 
        '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', 
        '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
          'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
120
120
120

加法底层也是调用的__add__方法

所有数值运算底层就调用的这些特殊方法



a=20
b=100
c=a+b
d=a.__add__(b)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
stu1=Student('张三')
stu2=Student('李四')
#c=stu1+stu2这样会报错
c=stu1+stu2#当在类里面定义add方法时就可以执行加法运算
c=stu1.__add__(stu2)
print(c,d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
a=[1,2,3,4,5]
print(len(a))#计算列表长度
print(a.__len__())
#当我想计算类的长度时需要在类中重写len方法
print(len(Student('jeck').name))#这里输出的为对象name的长度




#特殊属性
obj.__dict__                       对象的属性字典
obj.__class__                      对象所属的类
class.__bases__                    类的父类元组
class.__base__                     类的父类
class.__mro__                      类的层次结构
class._subclasses__()              类的子类列表

#__dict__获取对象或实例对象所绑定的所有属性和方法得字典
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name):
        self.name=name
a=A()
b=B()
x=C('jiec')#C类的实例属性
print(x.__dict__)#查看C类实例属性的字典
print(C.__dict__)#查看类对象的属性字典
print(A.__dict__,a.__dict__)
print(B.__dict__,b.__dict__)


print()
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)#C类的父类型元素
print()
print(A.__base__)
print(B.__base__)
print(C.__base__)#离它最近的父类
print()
print(A.__mro__)#类的层次结构
print(B.__mro__)#类的层次结构
print(C.__mro__)#类的层次结构
print()
print(A.__subclasses__())#找出子类
print(B.__subclasses__())#找出子类
print(C.__subclasses__())#找出子类

print()
print(A.__class__)#输出对象所属类
print(B.__class__)#输出对象所属类
print(C.__class__)#输出对象所属类




{'name': 'jiec'}
{'__module__': '__main__', '__init__': <function C.__init__ at 0x0000015991B6E950>, '__doc__': None}
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None} {}       
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None} {}       

(<class 'object'>,)
(<class 'object'>,)
(<class '__main__.A'>, <class '__main__.B'>)

<class 'object'>
<class 'object'>
<class '__main__.A'>

(<class '__main__.A'>, <class 'object'>)
(<class '__main__.B'>, <class 'object'>)
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

[<class '__main__.C'>]
[<class '__main__.C'>]
[]

<class 'type'>
<class 'type'>
<class 'type'>

############################################################类的深拷贝与浅拷贝#############################################################
变量的赋值：只是形成两个变量，实际上还是指向一个对象（python中一切皆对象）
或者说对象的赋值

class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,dick):
        self.cpu=cpu
        self.disk=dick

cpu=Cpu()
disk=Disk()

#创建计算机对象
com=Computer(cpu,disk)   #传入俩个对象

#变量（对象）的赋值
com1=com
print(com)
print(com1)

# <__main__.Computer object at 0x000001E5DBEF3010>
# <__main__.Computer object at 0x000001E5DBEF3010>

# 内存地址相同，即com赋值com1后是一个对象
print()
print('子对象地址',com.cpu,com.disk)

# 子对象地址 <__main__.Cpu object at 0x000001E06B58A980> <__main__.Disk object at 0x000001E06B633040>


print('子对象2内存地址',com1.cpu,com1.disk)


# <__main__.Computer object at 0x0000022C98BD3010>
# 子对象地址也是相同的

# 故变量的赋值或者说对象的赋值，其实际上在内存中只有一个对象（内存中只存一个对象（快递驿站），由不同取件码）




浅拷贝：拷贝时，对象包含的子对象内容不拷贝，故源对象与拷贝对象会引用同一个子对象
会产生一个新对象，但是子对象不会产生新的
也需要导入copy库



import copy



class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,dick):
        self.cpu=cpu
        self.disk=dick

cpu=Cpu()
disk=Disk()

#创建计算机对象
com=Computer(cpu,disk)   #传入俩个对象

com2=copy.copy(com)   #com2是新产生的对象，com2的子对象cpu，disk不变
print(com,com2,sep='---->')
# <__main__.Computer object at 0x000001D105A63040>----><__main__.Computer object at 0x000001D105A62D10>

#输出子对象
print(com,com.cpu,com2.disk)
print('-'*70)
print(com2,com2.cpu,com2.disk)

# <__main__.Computer object at 0x000001D6B7123EB0> <__main__.Cpu object at 0x000001D6B7123FD0> <__main__.Disk object at 0x000001D6B7123EE0>
# ----------------------------------------------------------------------
# <__main__.Computer object at 0x000001D6B7123B80> <__main__.Cpu object at 0x000001D6B7123FD0> <__main__.Disk object at 0x000001D6B7123EE0>
# com，和com2地址不同，但是子对象cpu和disk地址相同




深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，元对象和拷贝对象所有的子对象也不相同






import copy



class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,dick):
        self.cpu=cpu
        self.disk=dick

cpu=Cpu()
disk=Disk()

#创建计算机对象
com=Computer(cpu,disk)   #传入俩个对象


#浅拷贝

com2=copy.copy(com)   #com2是新产生的对象，com2的子对象cpu，disk不变
print(com,com2,sep='---->')
# <__main__.Computer object at 0x000001D105A63040>----><__main__.Computer object at 0x000001D105A62D10>

#输出子对象
print(com,com.cpu,com2.disk)
print('-'*70)
print(com2,com2.cpu,com2.disk)


# <__main__.Computer object at 0x000002793ECB3EB0> <__main__.Cpu object at 0x000002793ECB3FD0> <__main__.Disk object at 0x000002793ECB3EE0>
# ----------------------------------------------------------------------
# <__main__.Computer object at 0x000002793ECB3B80> <__main__.Cpu object at 0x000002793ECB3FD0> <__main__.Disk object at 0x000002793ECB3EE0>

#深拷贝
com3=copy.deepcopy(com)   #com3是新产生的对象，com3的子对象cpu，disk也会从新产生

#输出子对象
print(com,com.cpu,com.disk)
print('-'*70)
print(com3,com3.cpu,com3.disk)


# <__main__.Computer object at 0x000002793ECB3EB0> <__main__.Cpu object at 0x000002793ECB3FD0> <__main__.Disk object at 0x000002793ECB3EE0>
# ----------------------------------------------------------------------
# <__main__.Computer object at 0x000002793ECD4760> <__main__.Cpu object at 0x000002793ECD4640> <__main__.Disk object at 0x000002793ECD45E0>

# 新对象地址变，且子对象cpu和disk地址也变




'''
t=666