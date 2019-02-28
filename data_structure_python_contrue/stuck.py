from collections import deque
class Node(object):
    __slots__ = ('value','prev','next')   #固定属性
    def __init__(self,value=None,prev=None,next=None):
        self.value,self.prev,self.next=value,prev,next


class CircularDoubleLinkedList(object):
    #循环双端链表
    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        node=Node()
        node.next,node.prev=node,node
        self.root=node
        self.length=0
    def __len__(self):
        return self.length
    def headnode(self):    # 生成头结点 ，就是根结点的下一个

        return self.root.next
    def tailnode(self):
        return  self.root.prev  #尾结点，根结点的上一个
    def append(self,value):
        if self.length is not None and len(self) >= self.maxsize:
            raise Exception('LinkList is full')
        node = Node(value=value)
        tailnode=self.tailnode() or self.root
        #往后加入的过程
        tailnode.next=node
        node.prev=tailnode
        node.next= self.root
        self.root.prev=node
        self.length += 1
    def appendleft(self,value):
        if self.length is not None and len(self) >= self.maxsize:
            raise Exception('LinkList is full')
        node = Node(value=value)

        #往前加入的过程
        if self.root.next is self.root:   #空链表
            node.next=self.root
            node.prev = self.root
            self.root.prev=node
            self.root.next=node


        else:
            node.prev=self.root
            headnode=self.root.next
            node.next=headnode
            headnode.prev=node
            self.root.next=node
        self.length += 1
    def remove(self,node):    #这里传入的是node，而不是value，降低了时间复查度，可以达到O（1）
        if node is self.root : #空链表
            return
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.length -= 1
        return node
    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode =  self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        #这里由于只是遍历到了尾结点的前一个，所以退出循环后还要yield一个出来
        yield curnode
    def __iter__(self):
        for node in self.iter_node():
            yield node.value


    def iter_node_reverse(self):    #反序遍历
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

######################################################
# 下边是 Queue 实现
######################################################
class Deque(CircularDoubleLinkedList):   # 注意这里我们用到了继承，嗯，貌似我说过不会用啥 OOP 特性的，抱歉

    def pop(self):
        #删除尾结点
        if len(self) == 0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value
######################################################
# 下边是 stack 实现
######################################################

class Stack(object):
    def __init__(self):
        self._deque= deque()
    def pop(self):
        return self._deque.pop()
    def push(self,value):
        self._deque.append(value)

    def empty(self):
        return len(self._deque) == 0

