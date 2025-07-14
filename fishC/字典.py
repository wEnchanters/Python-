# 创建字典
# 1.直接大括号+：
x = {"吕布":"13", "关于":"14"}
print(type(x))

# 2.dict()
print(dict(吕布 = "lvbu", 关羽 = "guanyu"))

# 3.数组里面是元祖
print(dict([("吕布", "lvbu"), ("关羽", "guanyu")]))

# 4.5
print(dict({"吕布":"13", "关于":"14"}))

print(dict({"吕布":"13", "关于":"14"}, 刘备 = "刘备"))
# zip
print(dict(zip(["吕布","关羽"],["lvbu", "guanyu"])))

# 创建value一样的字典
d = dict.fromkeys("Fish", 250)
print(d)
# 删除，不存在时，返回设置值
d.pop('F', "没有")
print(d)
del d['i']
print(d)

# 修改，不存在的会新增
d['s'] = 115
print(d)
d.update({'i': 777, 'j': 888})
print(d)
d.update(F = '70', C = '67')
print(d)

# 查找
print(d.get('D', 0))
print('D' in d)

#当不存在就设置（只会新增）
print(d.setdefault('c', "code"))
print(d)

# 遍历 item value keys
print(d.values())
print(d.keys())
print(d.items())

# 拷贝
d2 = d.copy()
print(d.copy())
print(d == d2)

# 嵌套
d = {"吕布": {"语文":60, "数学":70, "英语":80}, "关羽": {"语文":1, "数学":2, "英语":3}}
for name, scores in d.items():
    s = ",".join([f"{subject}是{score}" for subject, score in scores.items()])
    print(f"{name}成绩：{s}")

c = {k:v for k,v in d.items()}
print(c)