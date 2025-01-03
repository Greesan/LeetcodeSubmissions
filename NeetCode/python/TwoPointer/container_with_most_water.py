class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #time complexity: O(n) --> iterating through array once through left right pointers that won't overlap
        #space complexity: O(1) --> no extra collection structures are used
        l,r = 0, len(heights)-1
        maxA = 0
        while l<r:
            #area calc is minimum of lr heights times base of (l-r)
            a = (r-l)*min(heights[l],heights[r])
            maxA = max(maxA,a)
            #move left and right based on which height is lower
            (l,r) = (l+1,r) if (heights[l] <= heights[r]) else (l,r-1)
        return maxA