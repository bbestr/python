def sum(a,b):
    """求和
    :param a: 数a
    :param b:  数b
    :return: 和
    """
    return a+b
def print_line(char,time):
    """打印一行分隔符"""
    print(char * time)
def print_lines(char,time,n):
    """打印多行分隔符"""
    i = 0
    while i <= n:
        print_line(char,time)
        i += 1
