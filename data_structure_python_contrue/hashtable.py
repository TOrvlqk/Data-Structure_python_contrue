class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

'''下面定义hashtable的槽'''
class Slot(object):
    '''
        槽有三种状态：
        1.HashMaP.UNUSED(指没有被使用过和未冲突过的槽)
        2.使用过但是remove掉的槽,HashMap.EMPTY,里面可能还有key
        3.槽当前正在使用Slot结点
    '''
    def __init__(self,value,key):
        self.value,self.key=value,key
class HashTable(object):
    UNUSED= None
    EMPTY=Slot(None,None)
    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)  # 保持 2*i 次方
        self.length = 0
    @property
    def _load_factor(self):
        #load_factor  超过0.8重新分配
        return self.length /float(len(self._table))
    def __len__(self):
        return self.length
    def _hash(self,key):
        return abs(hash(key)%len(self._table))
    def find
