new_list = ["xiaohong","xiaolan","daming","xionger"]

"""插入元素"""
#直接添加到末尾
new_list.append("oiawueioaw")
#指定位置插入
new_list.insert(1,56)
#吧一个列表 添加到当前末尾
new_list.extend("rgdgrr")
for i in new_list:
    print(i)
print(new_list)
"""删除数据"""
#remove 删除第一个出现位置的匹配元素
new_list.remove("r")
print(new_list)
#count  方法
kk = new_list.count("r")
print(kk)
#len方法  求长度
lenlist = len(new_list)
print(lenlist)
#pop
new_list.pop(3)
print(new_list)
#del 关键字删除元素   包变量从内存删除
del new_list[1]
print(new_list)
#clear
new_list.clear()
print(new_list)

newlist = [1,2,3,5,9,8,23,6,67]
newlist.sort(reverse=True)
print(newlist)


