def dakai():
    file = open("test.txt","r",encoding="utf-8")
    text = file.read()
    print(text)
    return text
    file.close()
def xieru(shuju):
    file1 = open("test1xieru.txt","w")
    file1.write(shuju)
    file1.close()
def copy_wenjian():
    ok = dakai()
    xieru(ok)
def big_copy():
    file = open("test.txt","r",encoding="utf-8")
    file1 = open("testbig.txt","w")
    while True:
        text = file.readline()
        print(text)
        if len(text) == 0:
            break
        else:
            file1.write(text)
big_copy()
