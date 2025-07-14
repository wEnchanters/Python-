def myfunc():
    for i in range(3):
        print(i)


myfunc()

def myfunc(name):
    for index, value in enumerate(name):
        print(index, value)

myfunc("name")


def myfunc(name, do, when):
    print(f"{name} 在 {when} 的时候 {do}")
myfunc("小米", "吃饭", "周三")

# 方法的参数默认值和关键字参数都要放在最后，位置参数永远在前面
def myfunc(do, when, name = "小米",):
    print(f"{name} 在 {when} 的时候 {do}")
myfunc("吃饭", "周三", name = "小米")

# / 斜杠左边不能支持关键字参数
def myfunc(do, when, /, name = "小米"):
    print(f"{name} 在 {when} 的时候 {do}")
myfunc("吃饭", "周三", name = "小米")

# * 右侧只能支持关键字参数
def myfunc(do, when, *, name = "小米"):
    print(f"{name} 在 {when} 的时候 {do}")
myfunc("吃饭", "周三", name = "小米")

# 参数用*收集参数，实际上是打包成元组
def myfunc(*args):
    print(f"参数有：{len(args)}个， 参数一是：{args[0]}")
myfunc(1, 2, 3)

# 返回多个值，return会打包成元组
def myfunc(*args):
    return (len(args), sum(args))
print(myfunc(1, 2, 3))


# 参数用*和普通参数，调用方法需要指定关键字
# 所以上面用*可以保证后面用关键字参数
def myfunc(*args, a, b):
    print(args, a , b)
myfunc(1, 2, 3, a = 1, b = 2)

# **打包成字典
def myfunc(**kwargs):
    print(kwargs)
myfunc(a = 1, b = 2)

def myfunc(a, *b, **kwargs):
    print(a, b, kwargs)
myfunc(1, 1, 2, 3, x = 1, y = 2)

help(str.format)

# *解包
def myfunc(a, b, c, d):
    print(a, b, c, d)
myfunc(*(1, 2, 3, 4))
# **关键词参数解包
myfunc(**{'a': 1, 'b': 2, 'c': 3, 'd': 4})

# 作用域：局部变量，全局变量，函数里用global修饰变量可以修改全局变量
# nonlocal修饰的内部函数变量可以修改外部函数的变量
# LEGB：Local局部作用域，Enclosed：嵌套函数的外层函数作用域
# Global：全局作用域，Build-In：内部作用域

# 局部作用域和全局冲突，用global
# 外部函数作用域和局部作用域冲突，用nonLocal

# 闭包
def funcA(func):
    x = 880
    def funcB():
        # nonlocal
        nonlocal x
        func()
        x += 1
        print(x)
    return funcB

# 装饰器
@funcA
def func():
    pass
func()
func()

# 带参数的装饰器
def funE(msg):
    def funcF(func):
        x = 880
        def funcG():
            # nonlocal
            nonlocal x
            func()
            x += 1
            print(f"{x} {msg}")
        return funcG
    return funcF
@funE(msg="nb")
def funZ():
    pass
funZ()
funZ()


# lambda
f = (lambda x : x * x)
print(f(2))
print(list(map(lambda x : ord(x) + 10, "FishC")))
print(list(filter(lambda x : x % 2 == 0, range(10))))