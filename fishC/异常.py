try:
    1 / 0
except Exception as e:
    print(e)
finally:
    print("依旧执行")

try:
    # 异常链
    raise ValueError("值不正确") from ZeroDivisionError
except Exception as e:
    print(e)

# 判断
s = "FIs1h"
assert s == "FIsh"