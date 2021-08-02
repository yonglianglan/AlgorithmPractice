'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-31 13:54:48
LastEditors: Please set LastEditors
LastEditTime: 2021-07-31 14:27:29
FilePath: \AlgorithmPractice\DataStructure\Stack\stack.py
'''

class Stack(object):
    def __init__(self, max_size=9999):
        self.max_size = max_size
        self.data = []
        self._count = 0
        
    def __len__(self):
        return self._count

    def pop(self):
        assert self._count>0
        output = self.data.pop(-1)
        self._count -= 1
        return output
    
    def empty(self):
        if self._count<=0:
            return True
        else:
            return False
        
    def push(self, x):
        self.data.append(x)
        self._count += 1


        
