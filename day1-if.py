import random
a = 19
if a>=18:
    print("可以进网吧")

    print("回家写作业")

print("哈哈哈哈")

player = int(input("请输入你输入的你要出的拳"))

computer = 1

print("玩家出的是%d  - 电脑出的是%d" %(player,computer))

#随机数  函数
aa  = random.randint(1,10)
print(aa)

i = 0
sumou = 0
sumji = 0
while i < 100:
    if i % 2 == 0:
        sumou += i
    else:
        sumji += i
    i += 1
print("偶数和:%d"% sumou)
print("奇数和 : %d" %sumji)

