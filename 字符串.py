i = "aw doajwojawoi34383fja"
i1 = ""
k= i.isspace()
print(k)

#只能判断整数
k = i1.isdecimal()

#isdigital isnumeric可以判断(1) 或'\u002b'   numeric还可判断汉字数字
print(i1.isdigit())
print(i1.isnumeric())
print(k)

#判断字符开头结尾
hello = "hello world llo"
print(hello.startswith("hello"))
print(hello.endswith("llo"))

#查找指定字符串
print(hello.find("llo"))
print(hello.find("oiu"))

#替换字符   生成了新的字符串
print(hello.replace("world","people"))
print(hello)
