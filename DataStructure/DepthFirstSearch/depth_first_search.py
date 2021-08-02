'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-31 10:54:52
LastEditors: Please set LastEditors
LastEditTime: 2021-07-31 15:10:52
FilePath: \AlgorithmPractice\DataStructure\DepthFirstSearch\depth_first_search.py
'''



from ..Stack import stack


class DepthFirstSearch(object):
    
    def __init__(self, start_node='v1'):
        self.search=[]
        self.mark=[]
        self.stack = stack()
        self.search.append(start_node)
        self.stack.push(start_node)
        self.mark.append(start_node)
        
    def __call__(self, input):
        self.dfs(input)
        return self.search
        
    def dfs(self, input):
        
        while not self.stack.empty():
            node = self.stack.pop()
            
            while node in input.keys():
                for sub_node in input[node]:
                    print(sub_node)
                    if sub_node not in self.mark:
                        self.search.append(sub_node)
                        self.mark.append(sub_node)
                        self.stack.push(sub_node)
                current_node = self.stack.pop()
                print("current node",current_node)
                node = current_node
            node = self.stack.pop()
        # return self.search
                

    
                    
                        
                        

    

    