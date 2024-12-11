from collections import defaultdict
class Solution:
    def mapify(self, s:str) -> defaultdict():
        d = defaultdict()
        for char in s:
            d[char] = d.get(char,0) + 1
        return d
    def isAnagram(self, s: str, t: str) -> bool:
        if self.mapify(s) == self.mapify(t):
            return True
        return False