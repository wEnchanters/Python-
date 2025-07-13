import random
ran = random.randint(1, 100)
count = 3
while count > 0:
    guess = int(input("猜想数字："))
    if guess == ran:
        print("猜的对！")
        print("但是没奖励")
        break
    elif guess > ran:
        print("太大了")
    else:
        print("太小了")
    count -= 1
print(ran)
# 李琦 = 'sb'
# x = 4
# y = 5
# x , y = y , x
# print('\"x, y\"')