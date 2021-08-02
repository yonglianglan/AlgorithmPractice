'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-31 10:01:56
LastEditors: Please set LastEditors
LastEditTime: 2021-07-31 10:42:36
FilePath: \AlgorithmPractice\DataStructure\Queue\queue.py
'''


class Queue(object):
    def __init__(self, max_size=9999):
        self.max_size = max_size
        self.data = []
        self._count=0
    
    def empty(self):
        if len(self.data)==0:
            return True
        else:
            return False
            
    def pop(self):
        assert len(self.data)>=1
        data = self.data.pop(0)
        self._count-=1
        return data
    
    def push(self, input):
        assert self._count < self.max_size
        self.data.append(input)
        self._count +=1
    
    def len(self):
        return self._count