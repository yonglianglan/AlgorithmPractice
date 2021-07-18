## -*- coding: utf-8 -*- 

'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-16 17:52:54
LastEditors: Please set LastEditors
LastEditTime: 2021-07-18 22:48:06
FilePath: /undefined/Users/xdf/Desktop/projects/python/insert_sort.py
'''

import random


class InsertSort(object):
    """
    算法思想： 依次将后面的数插入到前面合适的位置，直到所有数都插入合适。

    时间复杂度：${n^2}$


    """

    def __init__(self, inverse=False):
        self.inverse = inverse

    def __call__(self, input):
        output = self.insert_sort(input)
        return output

    def insert_sort(self, input):
        length = len(input)
        for i in range(1, length):  # 从2个元素开始进行插入
            for j in range(i):      # 第i个元素与前面n个元素比较交换位置，插入

                right = input[i-j]
                left = input[i-j-1]
                if not self.inverse:    # 从小到大排序
                    if right > left:
                        continue
                    else:
                        temp = left
                        input[i-j-1] = right
                        input[i-j] = temp
                else:                      # 从大到小排序
                    if right > left:
                        temp = left
                        input[i-j-1] = right
                        input[i-j] = temp
                    else:
                        continue
        return input


# random.seed(123)
random_num = [random.randint(i, 100)
              for i in range(random.randint(10, 30))]

# random_num = list(range(15)).sort()


insert_sost = InsertSort(inverse=False)
print("input data :{}\n".format(random_num))
insert_sorted = insert_sost(random_num)

print("sorted: {}".format(insert_sorted))
