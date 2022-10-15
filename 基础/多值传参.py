def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)
demo(1)
demo(1,2,3,4,5,6,name="xiaoming",range = 18)

def numsum(*args):
    sum  = 0
    list = args

    for i in  list:
        sum += i
    print(sum)

numsum(1,2,3,4,5,6,7,8,9,4)
