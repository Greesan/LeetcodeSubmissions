from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict()
        numsFreq = [[] for val in range(len(nums)+1)]
        for num in nums:
            numsDict[num] = numsDict.get(num,0) + 1
        for val,freq in numsDict.items():
            print(freq)
            numsFreq[freq].append(val)
        res = []
        for i in range(len(numsFreq)-1,0,-1):
            for val in numsFreq[i]:
                res.append(val)
                k-=1
                if k==0:
                    return res