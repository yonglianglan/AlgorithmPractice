
'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-15 00:12:02
LastEditors: Please set LastEditors
LastEditTime: 2021-07-15 01:21:58
FilePath: \BinarySearch\binary_search.py
'''

import random

class BinarySearch(object):

    """
    1、二分查找必须是有序类表
    2、选好起始查找位置，中间开始，减少一半的查找元素
    3、时间复杂度为 ${log_2 10}$
    
    """
    def __call__(self, search_list, num):
        output = self.search(search_list, num)
        return output

    def search(self, search_list, num):

        end = len(search_list)
        start = 0
        guess = (start + end) // 2
        
        while start < guess:
            if len(search_list) >= 1:
                if search_list[guess] == num:
                    return guess
                elif search_list[guess] > num:
                    end = guess
                else:
                    start = guess + 1
                guess = (start + end) // 2
            else:
                return None


random_list = random.sample(range(0,100),20)
random_list.sort()
binary_search = BinarySearch()
print("查找集合：{}".format(random_list))

output = binary_search(random_list, 10)
print("output:{}".format(output))

