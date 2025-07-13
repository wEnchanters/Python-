# 元组，不可变
rhyme = (1, 2, 3, 4, 5, "上山打老虎")

# 倒置
t = rhyme[::-1]
print(t)

# 全部
t = rhyme[:]
print(t)

# 查某元素的数目
print(rhyme.count(1))

# 元组拼接
s = (1, 2, 3)
t = (4, 5, 6)
print(s + t)
print(s * 3)
w = s , t
print(w)
# 遍历元组
for item in w:
    for each in item:
        print(each)

print([[item * 2 for item in row] for row in list(w)])

# 生成只有一个元素的元组，加一个“，”
x = (1, )
print(type(x))

# 打包和解包
# 打包
t = (123, 456, 789)
# 解包，左侧数目需要跟右侧一样
x, y, z = t
print(x, y, z)

# 除非用 *
x, *u = t
print(x, *u)

# 元组里可变的能修改
x = [1 ,2, 3]
y = (4, 5, 6, 10)
z = (x, y)
print(z)
z[0][0] = 9
print(z)