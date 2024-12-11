from typing import List
from collections import defaultdict
class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		#set impl
		s = set()
		for num in nums:
			if num in s:
				return True
			s.add(num)
			return False
		#dict impl-->uses more space
		'''
		d = defaultdict()
		for num in nums:
				if d.get(num,0) == 1:
					return True
				d[num] = 1
		return False
		'''
