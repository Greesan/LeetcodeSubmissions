class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        general idea: two pointer question: start from sides
        keep track of current max height on left and right (lmax, rmax)
        step in from left if lmax is less than or equal to rmax
        step in from right if rmax is less than lmax
        update lmax/rmax with stepped in value if needed depending on side that you step in from: max functions
        add in the current amount of water trapped from your stepped in side: res+=(l/r)max - height[(l/r)]
        '''
        #time complexity: O(n): iterating through array once, no overlap between l and r
        #space complexity: O(1): no extra data structure used
        #you can't have a trough given two or less heights
        if len(height) < 3:
            return 0
        l,r = 0,len(height)-1
        lmax,rmax = height[l],height[r]
        res = 0
        while l < r:
            if lmax <= rmax:
                l+=1
                lmax = max(lmax,height[l])
                res += lmax-height[l]
            else:
                r-=1
                rmax = max(rmax,height[r])
                res += rmax-height[r]
        return res