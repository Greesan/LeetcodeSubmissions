from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0
        r = l+1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] < prices[r]:
                maxProf = max(maxProf,prices[r]-prices[l])
            r+=1
        return maxProf