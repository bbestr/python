def num(*args,**kwargs):
    print(args)
    print(kwargs)
a = (1,2,3)
b = {"name" : "xiaoming","age":12}
num(a,**b)