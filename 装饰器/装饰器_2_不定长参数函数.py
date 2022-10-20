def set_fun(func):
    def call_fun(*args,**kwargs):
        print("装饰器!!!")
        func(*args,**kwargs)
    return call_fun
@set_fun
def test1(num,*args,**kwargs):
    print("test1-------",num)
    print("test1-------",args)
    print("test1-=-----",kwargs)

test1(20)
test1(20,(45,63,59))
test1(20,(45,63,59),name="xiaohong")
