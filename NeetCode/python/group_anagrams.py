from typing import List
from collections import defaultdict
class Solution:
    def listify(self,s: str) -> tuple[str]:
        ls = [0] * 26
        for char in s:
            ls[ord(char)-ord('a')]+=1
        return tuple(ls)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramdict = defaultdict()
        for s in strs:
            ls = self.listify(s)
            if ls in anagramdict:
                anagramdict[ls].append(s)
            else:
                anagramdict[ls] = [s]
        return(list(anagramdict.values()))
if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
