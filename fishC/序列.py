# 列表相加
print([1,2,3] + [3,4,5])
# 元组相加
print((1,2,3) + (4,5,6))
# 元组相乘
print((1,2,3) * 3)

# 列表可变
s = [1, 2, 3]
print(id(s))
s *= 2
print(id(s))

# 元组不可变
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))

# 清空列表
t = [1, 2, 3, 4, 5]
# 直接清空
del t[:]
print(t)

# 清空列表
t = [1, 2, 3, 4, 5]
# 直接清空
del t[0:len(t):1]
print(t)


# tuple，元组，列表可以互相转换
t = [1, 2, 3, 4, 5]
print(tuple(t))

# 最大最小值, 可以有默认值
print(max(t, default="无"))

# len注意大小，32位平台：2的31次方-1，64位平台：2的63次方-1
# print(len( 2**32))

# sum求和，可以给初始值
print(sum(t, 100))

# sort排序，reverse默认升序，可以用key指定用哪个属性
print(sorted(t, reverse= True))

# all函数为全真，any函数存在真
x = [1, 1, 0]
print(all(x))
print(any(x))
# enumerate 构成二元祖的列表，下标和值
seasons = ["Spring","Summer","Fall", "Winter"]
month = ["one","two","three", "four"]

for index, value in enumerate(seasons):
    print(index, value)

# zip创建可聚合多对象的迭代器，不一样长会以最短的为准
for item in zip(seasons, month):
    print(item)

import itertools
print(list(itertools.zip_longest(seasons, month, "不会丢掉长度不够的了")))

# map函数
print(list(map(ord, "FishC")))

print(list(map(pow, [1, 2, 3], [3, 4, 5])))

# 过滤函数
s = "Cnm"
print(list(filter(str.islower, s)))

# 获取迭代器，可以给默认值，当迭代到末尾的时候返回
x = [1, 2, 3, 4, 5]
y = iter(x, 0)
print(y)

# 多位数组排序
t = [[1, 2, 3], [4, 5, 6]]
print(sorted(t, key= lambda x : x[1]))