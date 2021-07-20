'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-18 23:02:52
LastEditors: Please set LastEditors
LastEditTime: 2021-07-18 23:49:54
FilePath: /AlgorithmPractice/DataStructure/Sort/QuickSort/quick_sort.py
'''

import random

class QuickSort(object):
	def __init__(self, inverse=False):
		self.inverse = inverse
	
	def __call__(self, disorder):
		output = self.sort(disorder)

	def sort_sub_disorder(self, recoder_idx, disorder):
		recoder = disorder[recoder_idx] 
		length = len(disorder)
	
		for i range(0,length,1):   
			if not self.inverse:
				if disorder[i] > recoder:
					temp = disorder[i]
					disorder[i] = recoder
					disorder[recoder_idx] = temp
					recoder = disorder[i]
					recoder_idx = i   
				else:
					continue
			else:
				if disorder[i] > recoder:
					continue
				else:
					temp = disorder[i]
					disorder[i] = recoder
					disorder[recoder_idx] = temp
					recoder = disorder[i]
					recoder_idx = i  
		return disorder
		
	def sort(self, disorder):
		lenght = len(disorder)
		recoder_idx = lenght // 2

		left_disorder = disorder[:recoder_idx]
		right_disorder = disorder[recoder_idx:]
		while len(disorder) > 1:
			recoder_idx = self.sort_sub_disorder(recoder_idx, disorder[:recoder_idx])
			left_disorder = disorder[:recoder_idx]
			right_disorder = disorder[recoder_idx:]
			order = self.sort(left_disorder)
			


		return order

