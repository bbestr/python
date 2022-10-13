def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
for i in range(1,20):
    print(fibo(i),end=" ")