'''冒泡排序'''

def bubble_sort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):   #后面的i个已经排好，无须再排
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]



'''选择排序'''
def select_sort(seq):
    for i in range(len(seq)-1):
        min_=i
        for j in range(i+1,len(seq)):
            if seq[j]< seq[min_]:
                min_= j
        if min_ != i :
            seq[i],seq[min_]=seq[min_],seq[i]


'''插入排序'''

def insertion_sort(seq):
    for i in range(1,len(seq)):    #第一个数就认为是有序的了
        pos = i
        while seq[pos]<seq[pos-1] and i>0:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = seq[i]
