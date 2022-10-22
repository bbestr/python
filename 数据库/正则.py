import re

def detect():
    names = ["age","_age","lage151","4565","/*/da","age+_","_________"]

    for i in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$",i)
        if ret:
            print("keyi")
        else:
            print("flase")


if __name__ == '__main__':
    detect()