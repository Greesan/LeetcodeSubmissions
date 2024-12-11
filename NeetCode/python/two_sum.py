from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums, target: int) -> List[int]:
        d = defaultdict()
        for i,num in enumerate(nums):
            if num in d:
                return [d[num],i]
            d[target-num] = i
        return [-1,-1]
if __name__ =="__main__":
    sol = Solution()
    print(sol.twoSum([3,4,5,6],7))
