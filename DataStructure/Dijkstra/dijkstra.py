'''
Author: lanyongliang
Email: 771857509@qq.com
Date: 2021-08-01 10:31:53
LastEditors: Please set LastEditors
LastEditTime: 2021-08-01 18:06:21
FilePath: \AlgorithmPractice\DataStructure\Dijkstra\dijkstra.py
'''


class Dijkstra(object):
    def __init__(self,start_node='start'):
        self.start_node = start_node
        
        
        
    def __call__(self, graph, cost):
        self.dijkstra(graph, cost)

    def get_lowest_cost_node(self, costs):
        node_cost = min(costs.items(), key=lambda x:x[1])
        return node_cost[0]

    def calculate_cost(self, neighbor_nodes, cost=0):

        for neighbor_node in neighbor_nodes:
            self.costs [neighbor_nodes] = cost + neighbor_nodes[neighbor_node]

    def dijkstra(self, graph):
        self.costs = {}
        self.parents = {}
        processed = []
        neighbor_nodes = graph[self.start_node]
        self.calculate_cost(neighbor_nodes)
        node = self.get_lowest_cost_node(self.costs)

        while node is not None:
            cost = self.cost[node]
            for neighbor in node.keys():
                self.calculate_cost(node,cost)
                new_cost = cost + node[neighbor]
                if self.costs[neighbor] > new_cost:
                    self.costs[neighbor] = new_cost
                    self.parents[neighbor] = node
            processed.append(node)




                
            
            


        

        
        