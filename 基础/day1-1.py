#格式化输出 %s 字符串
# %d 十进制整数 %f 浮点数 %.02f
# 代表 小数点保留两位 %% 输出%
import keyword
a = 45
b = 4.5632
c = 123456789
d = 20
print("我的年龄是%d"%a)
print("保留2位小数:%.3f"%b)
print("你是 %05d 大萨达" % c)

#字符串后跟 *n  表示将 字符串执行的指令重复 n次
print("占比 %d%%" %d * 5)

#关键词 所有的
print(keyword.kwlist)
