from pathlib import Path
p = Path.cwd()
print(p)
print(p.is_dir())
q = p/"文件存储测试.txt"
print(q.name)
# 文件名称没后缀
print(q.stem)
# 文件后缀
print(q.suffix)

parents = p.parents
for i in parents:
    print(i)

# 文件信息
print(p.stat())

print(p.stat().st_size)

# 相对路径
path = Path("./")
print(p.stat())
# 转换成绝对路径
print(p.resolve())

# 获取子文件对象
son = p.iterdir()
for s in son:
    print(s)

# 创建文件夹
print(Path("./niubi/Plus").mkdir(exist_ok=True, parents= True))

# 删除文件夹
print(Path.rmdir(Path("./niubi/Plus")))

# 搜索
for p in Path("./").glob(pattern= "**/*.py"):
    print(p)