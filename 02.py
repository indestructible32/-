# 导入随机模块
import random
# 嵌套循环
money = 10000
for i in range(1,21):
    n = random.randint(1, 10)
    if n < 5:
        print(f"员工{i},绩效分{n}，低于5，不发工资，下一位。")
        continue
    else:
        if money > 0:
            money -= 1000
            print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元")

        else:
            print("工资发完了，下个月再来领吧")
            break


# if money == 0:
#     print("工资发完了，下个月再领取吧。")
# else:
#     print(f"工资还剩{money}没发完")