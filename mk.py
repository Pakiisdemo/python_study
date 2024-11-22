
'''
每个模块中都包含一个模块名称变量_name_，程序可以在检查该变量，以确定他们在哪个模块运行，如果一个模块不希望在其他模块中运行，则其name'为_main_

'''
if __name__== '__main__':#这个__main__是判断是否是在本程序内运行
     print('MK中函数')
else:
    print('Other 模块')

t='tttttt'

def f(x):
    c=x**2
    return c

def infort():
    print('模块导入')
