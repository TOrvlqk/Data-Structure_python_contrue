'''快速排序'''

def quicksort(array):
    size = len(array)
    if not array or size < 2:  #  递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)



'''快排改进版'''
def patition(array,beg,end):
    pivot_index=beg
    pivot=array[pivot_index]
    left=pivot_index+1         #左右两边定义两个指针
    right=end-1
    while True:
        while array[left]<pivot and left<=right:
            left += 1
        while array[right]>=pivot and left<=right:
            right -= 1
        if left>right:
            break
        else:
            array[left],array[right]=array[right],array[left]
    array[right],array[pivot_index]=array[pivot_index],array[right]
    return right    #返回新的 pivot位置
def quicksort_inplace(array,beg,end):
    if beg < end :   #beg == end的时候为递归出口
        pivot=patition(array,beg,end)
        quicksort_inplace(array,beg,pivot)
        quicksort_inplace(array,pivot+1,end)
