# 创建集合 (unOrderSet?)
# 无序的
t = {"Fish", "Python"}
print(type(t))
print({s for s in t})

# 检查集合是否元素毫无相干
print(t.isdisjoint({"Fish", "java"}))
# 子集
print("子集")
print(t.issubset("FishJavaMen"))
print(t.issubset({"Fish", "Java", "C"}))
print(t.issubset({"Fish", "Java", "C"}))
print(t <= {"Fish", "Python"})

# 超集
print(t.issuperset({"Fish"}))
print(t > {"Fish", "Python"})
# 并集
print(t.union({1,2,3}))
print(t | {1, 2, 3})

# 交集
print(t.intersection({"Fish", "Java", "C"}))
print(t and {"Fish", "Java", "C"})
# 差集，左边不在右边里面
print(t.difference({"Fish", "Java", "C"}))
print(t - {"Fish", "Java", "C"})
# 对称差集，两边的不同
print(t.symmetric_difference({"Fish", "Java", "C"}))
print(t ^ {"Fish", "Java", "C"})

# 不可变集合
t = frozenset("FishC")

# 更新
s = set("FishC")
print(s)
s.update([1, 1], "Python")
print(s)
s.intersection_update("FishC")
print(s)
s.difference_update("shCD")
print(s)
s.symmetric_difference_update("ishC")
print(s)

s.add("45")
print(s)
# remove不存在会抛异常，discard会沉默
s.remove("F")
print(s)
s.discard("Sc")
print(s)

# 随即弹元素
print(s.pop())
print(s)

# 不可变的对象可哈希，可变对象不可哈希
# 可hash的才能当作字典的建以及集合的元素
# t = {[123]}

import random
h = [random.randint(1, 1000) for i in range(1000)]
print(h)