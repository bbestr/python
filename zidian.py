xiaomin = {"name":"xiaoming",
           "age":25,
           "weight":62}
for i in xiaomin:
    print(xiaomin.get(i))

print(len(xiaomin))

temp = {"major":"软件"}

xiaomin.update(temp)

print(xiaomin)

print(xiaomin.get("name"))
xiaomin.clear()
print(xiaomin)