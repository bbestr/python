import 类

ai = 类.Cat("皮蛋")

ai.eat()


try:
    i = int(input("输入"))
    num = 8
    num /= i
    print(num)
except ValueError:
    print("请输入正确的数字")
except ZeroDivisionError:
    print("除零异常")
else:
    print("正确执行完成")
finally:
    print("程序结束")

def dadain():
    i = input("请输入密码:")
    if len(i) < 8:
        AW = Exception("密码果断")
        raise AW
    else:
        print("成功")
try:
    dadain()
except Exception as result:
    print(result)
