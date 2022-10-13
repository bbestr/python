find_name = "亚索"
find_name1 = "大狗"
ste = [{"name":"亚索"},{"name":"瑞文"}]
for i in ste:
    print(i)
    if i["name"] == find_name1:
        print("找到了")
        break
else:
    print("没有找到")