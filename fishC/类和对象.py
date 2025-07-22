class LQ:

    __lq = 0

    def __init__(self, lq):
        self.__lq = lq
    def set_lq(self, lq):
        self.__lq = lq
    def get_lq(self):
        return self.__lq

class LQSON(LQ):

    # 限制不浪费空间，继承至父类的slots属性是不会生效的
    __slots__ = ["x", "y"]

    # 单横线开头的变量是内部变量
    def __init__(self, lq):
        self.x = 10
        _internalVariables = ""
        super().__init__(lq)


# 比init还要先执行的方法：__new__
class CapStr():

    def __init__(self, function, name):
        self.function = function
        self.name = name


#销毁的方法
    def __del__(self):
        self.function(self)
def outter():
    x = 0
    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x
    return inner

out = outter()

cs = CapStr(out, "lqSb")
print(cs.name)
del cs
t = out()
print(t.name)


# 属性访问相关的
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __getattribute__(self, item):
        print("拦截")
        return super().__getattribute__(item)

c = C("lq", 45)
print(c.__getattribute__("name"))
# 私有变量还是不能访问
# print(c.__getattribute__("age"))
# 除了使用这种方式，不推荐
print(getattr(c, "_C__age"))

print(hasattr(c, "name"))

print(setattr(c, "name", "sblq"))

print(c.name)

print(delattr(c, "name"))
# name属性就没了
# print(c.name)


class D:
    def __setattr__(self, key, value):
        return super().__setattr__(key, value)

d = D()
d.__setattr__("name", "lq")
print(d.name)

# bool方法代偿是len
# in 会先去找ite和next，没有的话会找getItem

# 比较运算的魔法方法：
# < __lt__
# <= __le__
# > __gt__
# >=  __ge__
# == __eq__
# != __ne__

# 调用函数一样调用对象
class C:
    # *代表未知参数，**代表关键字参数
    def __call__(self, *args, **kwargs):
        print(f"位置参数 -> {args}\n关键字参数 -> {kwargs}")

c = C()
c(1,2,3,x=250,y=520)

class Power:
    def __init__(self, exp):
        self.exp = exp
    def __call__(self, *args):
        return args[0] ** self.exp
p = Power(3)
print(p(2))

# repr，感觉是represent，也就是显示的时候用的。会显示具体的值而不是地址
print(repr('你好'))
# str，str的代偿是repr
print(str("你好"))

class C:
    # def __repr__(self):
    #     return "repr"
    def str(self):
        return "repr"
cs = [C(), C(), C()]
print(cs)

for each in cs:
    print(each)

class E:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    # def delX(self, x):
    #     super().__delattr__(self, x)
    @x.deleter
    def x(self):
        del self._x

e = E("property装饰器")
print(e.x)
e.x = "lq"
print(e.x)

# classmethod方法
class C:
    count = 0
    @classmethod
    def add_count(cls):
        cls.count += 1

    def __init__(self):
        self.add_count()
    @classmethod
    def get_count(cls):
        return cls.count

class D(C):
    count = 0
c1 = C()
c2 = C()
c3 = C()
print("实例化次数计算")
print(c3.get_count())
d1 = D()
print(d1.get_count())

# 静态函数 @staticmethod
class C:
    @staticmethod
    def func():
        print("静态方法")
C.func()

# 描述符号和property实例
class D:
    def __get__(self, instance, owner):
        print(f"get~\nself -> {self}\ninstance -> {instance}\nowner -> {owner}")
    def __set__(self, instance, value):
        print(f"get~\nself -> {self}\ninstance -> {instance}\nvalue -> {value}")
    def __delete__(self, instance):
        print(f"get~\nself -> {self}\ninstance -> {instance}\n")

# 描述符只能用于类属性
print("描述符只能用于类属性")
class Description:
    def __get__(self, instance, owner):
        print("get~")
class C:
    x = Description()
c = C()
c.x

# 数值描述符
# 对象属性
# 非数值描述符
# 类属性

