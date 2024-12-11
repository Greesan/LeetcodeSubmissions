class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        lower = s.lower()
        while l<r:
            while l<r and not lower[l].isalnum():
                #print("l" + str(s[l]))
                l+=1
            while r>l and not lower[r].isalnum():
                #print("r" + str(s[r]))
                r-=1
            #print("lind:"+ str(l) + "\trind:" + str(r))
            #print("l:"+ str(s[l]) + "\tr:" + str(s[r]))
            if lower[l]!=lower[r]:
                return False
            l,r = l+1,r-1
        return True