
arr = [21,56,47,59,26,3,88,63,14,2,98,67,77,66,55,44,33]
def insert_sort(ar):

    for i in range(1,len(ar)):

        for j in range(i,0,-1):
            if ar[j] < ar[j-1]:
                ar[j],ar[j-1] = ar[j-1],ar[j]
    return ar
def erfen_query(a,target):
    low = 0
    high = len(a)

    while low < high:
        mid = (low+high) // 2
        print(a[mid])
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid
        else:
            high = mid
    return -1
def guibing_sort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar)//2
    left = guibing_sort(ar[:mid])

    right = guibing_sort(ar[mid:])

    l_p,r_p = 0,0
    result = []
    while l_p < len(left) and r_p < len(right):
        if left[l_p] < right[r_p]:
            result.append(left[l_p])
            l_p += 1
        else:
            result.append(right[r_p])
            r_p += 1
    result += left[l_p:]
    result += right[r_p:]

    return result
def maopao_sort(mp):

    for i in range(len(mp)-1):
        for j in range(len(mp)-i-1):
            if mp[j] > mp[j+1]:
                mp[j],mp[j+1] = mp[j+1],mp[j]

    return mp
def xier_sort(xr):
    n= len(xr)
    gap =n//2
    while gap>0:
        for j in range(gap,n):
            i= j
            while i>=gap and xr[i] < xr[i-gap]:
                if xr[i] < xr[i-gap]:
                    xr[i],xr[i-gap] = xr[i-gap],xr[i]
                    i-=gap
                else:
                    break
        gap //=2
    return xr
def xuanze_sort(qk):
    n = len(qk)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if qk[min] > qk[j]:
                min = j
        qk[i],qk[min] = qk[min],qk[i]

    return qk
def qiuck_sort(qkk,left,right):
    if left >= right:
        return
    mid_value = qkk[left]
    low = left
    n = len(qkk)
    high = right
    while low < high:
        while low<high and qkk[high] >= mid_value:
            high -= 1
        qkk[low] = qkk[high]
        while low<high and qkk[low] < mid_value:
            low += 1
        qkk[high] = qkk[low]

    qkk[low] = mid_value
    qiuck_sort(qkk,left,low-1)
    qiuck_sort(qkk,low+1,right)


if __name__ == '__main__':
    # a = insert_sort(arr)
    # print("插入排序:\n",arr)
    #
    # find = erfen_query(a,26)
    # print("二分查询:",find)

    # guib = guibing_sort(arr)
    # print("归并排序:",guib)

    # mao = maopao_sort(arr)
    # print("冒泡排序:",mao)

    # xire = xier_sort(arr)
    # print("希尔排序:",xire)

    # quick = xuanze_sort(arr)
    # print("选择排序:",quick)

    qk = qiuck_sort(arr,0,len(arr)-1)
    print("快速排序:",arr)

