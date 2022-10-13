#函数
def chengfa():
    """九九乘法"""
    i = 1
    while i <= 15:
        k = 1
        while k <= i:
            print("%d*%d=%d"%(k,i,i*k),end="\t")
            k += 1
        print()
        i += 1