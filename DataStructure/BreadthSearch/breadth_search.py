'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-31 09:09:41
LastEditors: Please set LastEditors
LastEditTime: 2021-07-31 14:07:46
FilePath: \AlgorithmPractice\DataStructure\BreadthSearch\breadth_search.py
'''

# from queue import Queue


from ..Queue import queue

class BreadthSearch(object):
    def __init__(self, start_node='v1'):
        self.search=[]
        self.mark=[]
        self.queue = queue()
        self.queue.push(start_node)
        self.search.append(start_node)
        self.mark.append(start_node)
        

    def __call__(self, input):
        output = self.bfs(input)
        return output

    def bfs(self, input):
        
        while not self.queue.empty():
            node = self.queue.pop()
            print(node)
            if node in input.keys():
                for sub_node in input[node]:
                    self.queue.push(sub_node)
                    if sub_node not in self.mark:
                        self.search.append(sub_node)
                        self.mark.append(sub_node)
                    else:
                        continue
            else:
                continue
            # self.queue.get

        return self.search

