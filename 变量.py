num = 10
def sum():
    global num
    num = 20
    print(num)
def sum1():
    print(num)
sum()
sum1()