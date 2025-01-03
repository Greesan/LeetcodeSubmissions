from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            target = 0 - a
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r] > target:
                    r-=1
                elif nums[l]+nums[r] < target:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
        return res
