class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use set to make "in" lookups have average tc of O(1)
        #time complexity: O(n) --> while the while inside for might seem like O(n^2), by limiting the inner while to start from a subsequence beginning, this becomes O(n)
        #space complexity: O(n) --> use of extra set of space n
        numSet = set(nums)
        maxLen = 0
        for num in nums:
            # check if start of subsequence by ensuring no value before the current value exists in nums
            if num-1 not in numSet:
                length = 1
                #iteratively check through all consecutive values in array
                while num + length in numSet:
                    length +=1
                maxLen = max(maxLen, length)
        return maxLen