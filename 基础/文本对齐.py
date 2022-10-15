poem = ["静夜思",
        "李白 ",
        "  \t窗前明月光  ",
        "疑似地上霜",
        "举头望明月",
        "低头思故乡"]

for ie in poem:
    print("|%s|"% ie.strip().ljust(50," "))

str = "hello WORD "

print(str.title())
print(str.swapcase())
print(str.upper())
print(str.lower())
