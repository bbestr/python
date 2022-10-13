#缺省参数 在末尾
def gender(name,sex=True):
    sex_l = "男生"

    if not sex:
        sex_l = "女孩"
    print("%s 是 %s" %(name,sex_l))
gender("小明")
gender("小红",sex=False)