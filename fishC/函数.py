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

print("斐波那契数列")
def fibonacci_sequence(n):
    cache = {}
    def fib(value):
        if value in cache:
            return cache[value]
        elif value <= 1:
            return value
        cache[n] = fib(value - 1) + fib(value - 2)
        return cache[n]

    return [fib(i) for i in range(n + 1)]


print(fibonacci_sequence(10))

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
print(fib(10))

# 装饰器
@funcA
def func():
    pass
func()
func()
import functools

print("装饰器和注解")
# 带参数的装饰器
def funE(msg):
    def funcF(func):
        x = 880
        @functools.wraps(func)
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
funZ = funZ()

 

# lambda
f = (lambda x : x * x)
print(f(2))
print(list(map(lambda x : ord(x) + 10, "FishC")))
print(list(filter(lambda x : x % 2 == 0, range(10))))


# 生成器
print("生成器")
# 每次执行到yield时，返回一条数据，保存状态，等到下次调用在执行
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
for i in counter():
    print(i)

c = counter()
print(next(c))

def fib():
    first, second = 0 , 1
    while True:
        yield first
        first, second = second, first + second

print("递归")
def factInt(num):
    if num <= 1:
        return num
    return num * factInt(num - 1)

print(factInt(3))

print("汉诺塔")
def hanno(n, f, a, t):
    if (n == 1):
        print(f"从{f} 移动到 {t}")
        return
    hanno(n - 1, f , t, a)
    print(f"从{f} 移动到 {t}")
    hanno(n - 1, a , f, t)


hanno(2,  "F", "A", "T")

# /注释
def exchange(dollar:str, rate:int = 6.32) -> int:
    '''
    功能：
    参数：
    :param dollar:
    :param rate:
    :return:
    '''
    return dollar * rate
help(exchange)
# 类型注释

import functools
print(functools.reduce(lambda x,y:x * y, [1, 2, 3, 4]))

