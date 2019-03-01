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
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0
    @property
    def _load_factor(self):
        #load_factor  超过0.8重新分配
        return self.length /float(len(self._table))
    def __len__(self):
        return self.length
    def _hash(self,key):
        return abs(hash(key)%len(self._table))   #使用python内置的哈希函数
    def _find_key(self,key):            #找到return index ，找不到 return None
        index=self._hash(key)
        _len=len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index=(index*5+1)%_len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None
    def _find_slot_for_insert(self,key):
        index=self._hash(key)
        _len=len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index
    def _slot_can_insert(self,index):
        return (self._table[index] is  HashTable.UNUSED or self._table[index] is HashTable.EMPTY)
    def __contains__(self, item):   #定义in操作符
        index=self._find_key(key)
        return index is not None
    def add(self,key,value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value=value
            return False
        else:
            index =self._find_slot_for_insert(key)
            self._table[index]=Slot(key,value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
    def _rehash(self):
        old_table = self._table
        newsize = len(self._table)*2
        self._table=Array(newsize,init=HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1
    def get(self,key,default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self,key):
        index = self._find_key(key)
        if key is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = Slot(HashTable.EMPTY)
        return value
    def __iter__(self):    #python里遍历字典是默认遍历他的 key
        for slot in self._table:
            if slot  not in (HashTable.EMPTY,HashTable.UNUSED):
                yield slot.key











