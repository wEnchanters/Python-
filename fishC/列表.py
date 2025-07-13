rhyme = [1,2,3,4,5]
print(len(rhyme))
print(rhyme[-1])
print(rhyme[0:3])
print(rhyme[3:])
print(rhyme[:])
#跳跃
print(rhyme[0:len(rhyme):2])
print(rhyme[::2])
#倒序
print(rhyme[::-2])

# 新增
rhyme.append(6)
print(rhyme)
# 合并
hero = [777,888]
rhyme.extend(hero)
print(rhyme)
# 新增
rhyme[len(rhyme):] = [999]
print(rhyme)
# 新增到某个位置
rhyme.insert(1, 5555)
# 新增到末尾
rhyme.insert(len(rhyme), 44444)
print(rhyme)

# 删除第一个匹配的，不存在会报错
rhyme.remove(999)
print(rhyme)

# 删除某个位置
rhyme.pop(1)
print(rhyme)

# 多个元素的替换
print(hero)
hero[1:] = [1,2,3]
print(hero)

# 排序，默认升序
hero.sort(reverse=True)
print(hero)

#查询有几个
print(hero.count(1))

# 把元素替换
hero[hero.index(777)] = 888
print(hero)

# 找到元素位置
print(hero.index(888, 0, len(hero)))
print(hero)
hero2 = hero.copy()
hero2.append(1)
print(hero2)
print(hero)
hero2 = hero[1:]
print(hero2)

# 列表加法 乘法
s = [1, 2, 3, 4, 5]
t = [6, 7, 8, 9]
print(s + t)
print(s * 3)

# 列表嵌套
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
for i in matrix:
    for each in i:
        print(each, end=' ')
    print()

# 初始化列表
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
print(A)

# is运算符
x = [1, 2, 3]
y = [4, 5, 6]
print(x is y)

# 浅拷贝
import copy
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
matrix2 = copy.copy(matrix)
print(matrix)
print(matrix2)
matrix2[0][0] = 10000
print(matrix)
print(matrix2)

# 深拷贝
import copy
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
matrix2 = copy.deepcopy(matrix)
print(matrix)
print(matrix2)
matrix2[0][0] = 10000
print(matrix)
print(matrix2)

# 列表推导式
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
matrix = [i * 2 for i in matrix]
print(matrix)


matrix = [ord(i) for i in "FISH"]
print(matrix)

# 对角线
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
col = [matrix[i][i] for i in range(len(matrix))]
print(col)

# 反对角线
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]


col = [matrix[i][len(matrix[0]) - i - 1] for i in range(len(matrix))]
print(col)

s = [[0] * 3 for i in range(3)]
print(s)
s[0][1] = 1
print(s)
# 条件过滤1
even = [i for i in range(10) if i % 2 == 0]
print(even)
# 条件过滤2
world = [word for word in ["F", "FU", "cnm", "nv", "fuck"] if word.lower().startswith("f")]
print(world)
# 二维变一维
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

flatten = [col for row in matrix if row[0] == 1 for col in row]
print(flatten)

