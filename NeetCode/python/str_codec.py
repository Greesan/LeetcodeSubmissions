from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        bigStr = ""
        for s in strs:
            bigStr += (str(len(s)) + "|" + s)
        return bigStr
    def decode(self, s: str) -> List[str]:
        strList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j+=1
            intVal = int(s[i:j])
            strList.append(s[j+1:j+intVal+1])
            i = j+intVal+1
        return strList