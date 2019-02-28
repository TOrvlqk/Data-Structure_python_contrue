class Array(object):

    def __init__(self,size=32):
        self._size= size
        self._items=[None]*size
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, key, value):
        self._items[key]=value
    def __len__(self):
        return  self._size
    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i]=value
    def __iter__(self):
        for item in self._items:
            yield item


'''以下开始用数组实现队列'''


class FullError(Exception):  #自定已满错误
    pass
class EmptyError(Exception):    #定义空队列错误
    pass
class ArrayQueue(object):
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.array=Array(maxsize)
        self.head=0
        self.tail=0
    def push(self,value):
        if len(self) >=self.maxsize:
            raise FullError('队列已满')
        self.array[self.head % self.maxsize]=value
        self.head += 1
    def pop(self):
        if self.head == 0 :
            return EmptyError('列表为空')
        value=self.array[self.tail % self.maxsize]
        self.tail += 1
        return value
    def __len__(self):
        return  (self.head - self.tail)


