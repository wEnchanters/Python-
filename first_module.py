g_num = 100
def show():
    print('hhhh')
class Student(object):
    def __init__(self, name, age):
        print('111')# 必须要有 name 和 age 参数
        self.name = name
        self.age = age
    def show_msg(self):
        print(self.name, self.age)
if __name__ == '__main__':
    show()