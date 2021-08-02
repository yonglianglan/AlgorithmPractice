'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-08-03 00:35:08
LastEditors: Please set LastEditors
LastEditTime: 2021-08-03 01:33:05
FilePath: /AlgorithmPractice/DataStructure/LinkList/link_list.py
'''


class Node(object):
    def __init__(self,item):
        self.next=None
        self.item=item
    



class SingleLinkList(object):
    def __init__(self):
        self._head = None
        self._count = 0

    def empty(self):
        if self.next==None:
            return True
        else:
            return False
        
    def insert(self, index, item):
        new_node = Node(item)
        curr_node = self._head
        count = 0
        if index <=0:
            self._head=new_node
        elif index >=self.__len__():
            while curr_node is not Node:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:

            while curr_node is not Node:

                curr_node = curr_node.next
                if count == index:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                    break
                count +=1
            


    def append(self, item):
        node = Node(item)
        length = self.__len__()
        if length == 0:
            self._head = node
        else:
            curr_node = self._head
            for i in range(length):
                curr_node = curr_node.next

            curr_node.next = node
    
    def delete(self, index):
        assert self.__len__() >= index
        curr_node = self._head
        for i in range(index-1):
            curr_node = curr_node.next
        curr_node.next = None
        

        




node1 = Node(1)
node2 = Node(2)
link_list = SingleLinkList()
link_list._head=node1
node1.next=node2





