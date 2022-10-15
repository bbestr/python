def demo(num,numlist):
    numlist += num
    print(numlist)
num = [1,2,3]
numlist = [4,5,6]
print(numlist)
demo(num,numlist)
print(numlist)
# 针对列表  +=  相当于 extend   会修改外部数据