'''
二分查找(必须是有序的数列)普通实现
beg为猜测头  end为猜测尾
'''
def binary_search(sort_array,value):

    if not sort_array :
        return -1
    beg =0
    end = len(sort_array)-1
    while beg<end:
        mid= int((beg+end)/2)
        if sort_array[mid] == value:
            return mid
        elif sort_array[mid]>value:
            end= mid - 1
        else:
            beg= mid + 1
    return -1

'''递归实现'''
def binary_search2(sort_array,beg,end,value):
    if not sort_array:
        return -1
    mid = int((beg+end-1)/2)
    if beg>end:
        return -1
    if sort_array[mid]==value:
        return mid
    elif sort_array[mid]>value:
        return binary_search2(sort_array,beg,mid-1,value)
    else:
        return binary_search2(sort_array,mid+1,end,value)


