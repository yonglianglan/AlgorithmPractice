'''
Author: lanyongliang
Email: lanyongliang@xdf.cn
Date: 2021-07-18 23:02:52
LastEditors: Please set LastEditors
LastEditTime: 2021-07-21 01:41:10
FilePath: \AlgorithmPractice\DataStructure\Sort\QuickSort\quick_sort.py
'''

import random

class QuickSort(object):
	def __init__(self, inverse=False):
		self.inverse = inverse
	
	def __call__(self, disorder):
		length = len(disorder)
		self.sort(disorder, 0, length-1)


	def partion(self, disorder, left, right, inverse=False):

		recoder_idx = left
		recoder = disorder[recoder_idx]
		if not inverse:
			while(left < right):
				while(left < right and recoder <= disorder[right]):
					right -=1
				# temp = recoder
				disorder[left] = disorder[right]
				# right -=1

				while(left < right and recoder >= disorder[left]):
					left +=1
					recoder_idx = left
				# temp = disorder[left]
				# disorder[left] = recoder
				disorder[right] = disorder[left]
			disorder[recoder_idx] = recoder

		# else:

		return recoder_idx

	def sort(self, disorder, left, right):
		if left < right -1:
			recoder_idx = self.partion(disorder, left, right)
			print("recoder:{}".format(recoder_idx))
			self.sort(disorder, left, recoder_idx-1)
			self.sort(disorder, recoder_idx+1, right )
		else:
			return disorder

random_num = [random.randint(i, 100)
              for i in range(random.randint(8,12))]
quick_sost = QuickSort(inverse=False)
print("input data :{}\n".format(random_num))
quick_sost(random_num)
print("sorted: {}".format(random_num))