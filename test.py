'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-31 10:10:11
LastEditors: Please set LastEditors
LastEditTime: 2021-08-01 18:03:56
FilePath: \AlgorithmPractice\test.py
'''

from DataStructure.BreadthSearch import BreadthSearch
from DataStructure.DepthFirstSearch import DepthFirstSearch
from DataStructure.Dijkstra import dijkstra


def test_bfs():
    graph={}
    graph['v1'] = ["v2","v3"]
    graph['v2'] = ['v4','v5']
    graph['v3'] = ['v6','v7']
    graph['v6'] = ['v7']
    graph['v4'] = ['v8']
    graph['v5'] = ['v8']

    bfs = BreadthSearch()
    output = bfs(graph)
    print(output)

def test_dfs():
    graph={}
    graph['v1'] = ["v2","v3"]
    graph['v2'] = ['v4','v5']
    graph['v3'] = ['v6','v7']
    graph['v6'] = ['v7']
    graph['v4'] = ['v8']
    graph['v5'] = ['v8']

    dfs = DepthFirstSearch()
    output = dfs(graph)
    print(output)

def test_dijkstra():
    graph={}
    graph['start'] = {"黑胶唱片":5,"海报":0}
    graph["黑胶唱片"] = {"吉他":15,"架子鼓":20}
    graph["海报"] = {"吉他":30, "架子鼓":35}
    graph["吉他"] = {"钢琴":20}
    graph["架子鼓"]={"钢琴":10}
    dja = dijkstra()
    output, cost = dja(graph)
    print(output, cost)

test_bfs()
test_dfs()
test_dijkstra()