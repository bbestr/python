def set_fun(func):
    def call_fun(*args,**kwargs):
        print("装饰器1111!!!")
        return func(*args,**kwargs)
    return call_fun
def set_fun1(func):
    def call_fun1(*args,**kwargs):
        print("装饰器2222!!!")
        return func(*args,**kwargs)
    return call_fun1

@set_fun1
@set_fun
def test(num,*args,**kwargs):
    print("test1-------", num)
    print("test1-------", args)
    print("test1-=-----", kwargs)
    return "ok"

print(test(20))