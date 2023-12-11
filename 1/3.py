def binary_search(num,array,start = 0, end = 0):
    if end == 0:
        end = len(array)-1
    if start > end:
        return False
    mid = (start+end)//2
    if array[mid] == num:
        return mid
    elif array[mid] > num:
        return binary_search(num,array,start,mid-1)
    else:
        return binary_search(num,array,mid+1,end)

print(binary_search(7,[2,3,4,7,8]))