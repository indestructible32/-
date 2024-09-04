# 导入随机模块
import random

# 得到一个随机的 1 ~ 100 以内的数字
number = random.randint(1,100)
count = 0
n = int(input("我想好了,请您开始猜吧！"))
count = count + 1

# 用 while 循环和 if 语句判断
while n != number:

    if n > number:
        n = int(input("大了大了,再试一次"))
        count += 1

    elif n < number:
        n = int(input("小了小了，再试一次"))
        count += 1

# 输出正确答案和猜数次数
print("\n恭喜您猜对了！就是%d" % n)
print("您猜了%d次就猜对了\n" % count)





