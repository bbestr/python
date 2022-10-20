def set_fun(func):
    def call_fun(num):
        print("装饰器!!!")
        func(num)
    return call_fun


@set_fun  #等价于 test = set_fun(test)
def test(a):
    print("-------------test--------")
    print(a)
@set_fun
def test1(a):
    print("-------------test1--------")
    print(a)
test(50)
test1(100)