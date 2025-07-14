x = "i Love China 6"
# 第一个字母大写
print(x.capitalize())
# 所有字母是小写，包括德语
print(x.casefold())
# 字符串每个单词首字母大写，其他字母小写
print(x.title())
# 大写变小写，小写变大写
print(x.swapcase())
# 所有字母变大写
print(x.upper())
# 所有字母变小写，只有英语
print(x.lower())
# 左中右对齐
x = "有内鬼，停止交易内"
# 中间对齐
print(x.center(15) + "!")
# 左边对齐，支持自定义填充
print(x.ljust(15, "n") + "!")
# 右边对齐
print(x.rjust(15) + "!")
# 前面填充0
print(x.zfill(15))
# 查找出现的次数
print(x.count("内"), 0, 5)
# 找字符串，找不到返回-1，index找不到会报错
print(x.find("内", 0 , 5))
print(x.rfind("内", 0 , 5))
# 替换tab为空格
x = "有内鬼，停止交易内  "
print(x.expandtabs(4) + "!")
# 替换字符串
print(x.replace("有内鬼", "无内鬼").replace("停止", "可以"))
# 打表
table = x.maketrans("ABCDEFG", "1234567", "love")
print("I love China".translate(table))
# 判断字符串是xx
x = "他爱python"
print(x.startswith(("你","我","她")))
# 是否字母都以大写开头，其他都小写
x = "I Love Python"
print(x.istitle())
# 全大写
print(x.isupper())
# 全字母
print(x.isalpha())
# 是空白字符串
print(x.isspace())
# 是否都是可打印字符
x = " \n"
print(x.isprintable())
# 是否数字
x = "12345"
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "2²"
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "IV"
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "一"
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

# 全是数字或者字母
print(x.isalnum())

# 是否合法变量标识符
print("52xstr".isidentifier())

# 判断是否保留关键字
import keyword
print(keyword.iskeyword("if"))

# 截取
# 默认不留白，可自定义不留的字符
x = "  左侧"
print(x.lstrip())
x = "www.niubi.com"
print(x.rstrip("wwwcom"))
# 两边都去除
print(x.strip())
# 去除指定字符串开头
print("去除指定")
x = "www.niubi.com"
print(x.removeprefix("www"))
print(x.removesuffix("com"))

# 根据分隔符分开，只需要一个
print(x.partition("."))
print(x.rpartition("."))

# 全部根据分隔符分开，默认空格，可以指定分隔次数
print(x.split("."))
print(x.rsplit(".", 1))

x = "你好\r好的\n牛逼\r\n"
# 根据换行符分割，可以带上换行符，默认不带换行符
print(x.splitlines())
print(x.splitlines(True))

x = "nb"
# 拼接
print(".".join(["LQ", "SB"]))
print("".join([x, x]))

# 占位符
year = 2010
print("成立于 {}".format(year))
print("成立于 %s" %year)
print("成立于 {0}, 喜欢{t}".format(year, t = "python"))


print("对齐")
# 对齐,"<左 >右 =符号后数字前 ^居中
print("{:^}".format(250))
print("{:^10}".format(250))
print("{1:>10}{0:<10}".format(444, 555))
# 这两者区别
print("{:1>10}".format(-420))
print("{:1=10}".format(-420))

print("{:+}{:}".format(250, -520))
print("{:,}".format(123456))

print("精度")
# 限定小数点后2位
print("{:.2f}".format(3.14159))
# 限定前后数位
print("{:.2g}".format(31.14159))
# 精度
print("{:.6}".format(3.14159))

# 二进制
print("{:b}".format(80))
# unicode
print("{:c}".format(80))
# 十进制
print("{:d}".format(80))
# 八进制
print("{:o}".format(80))
# 十六进制，#号可以加前缀
print("{:#x}".format(80))
print("{:X}".format(80))
# 跟d类似，会使用分隔符插入到恰当的位置
print("{:n}".format(80))
# 跟d一样
print("{:}".format(80))

print("浮点数")
# 浮点数
# 科学计数法
print("{:e}".format(3.14159))
print("{:E}".format(3.14159))
# 定点表示法
print("{:f}".format(3.14159))
print("{:F}".format(3.14159))
# 通用，小数以‘f’形式，大数以‘e’形式
print("{:g}".format(3.14159))
# 通用，小数以‘F’形式，大数以‘E’形式
print("{:G}".format(3.14159))
# 跟‘g’类似，只是会插入分隔符
print("{:n}".format(3.14159))
# 以百分比的形式输出（数字乘100并显示为定点表示法‘f’的形式，后面附带一个百分号）
print("{:%}".format(3.14159))
print("{:.2%}".format(3.14159))
print("{:.{prec}f}".format(3.14159, prec = 2))

# 格式
print("{:{fill}{align}{width}.{prec}{ty}}".format(3.14159, fill= '-', align = '>', width = 10, prec = 3, ty = 'g'))

year = 2000
align = '>'
width = 10
fill = '-'
print(F"成立于{year}年")
print(f"{year:010}")
print(f"{year:{fill}{align}{width}}")