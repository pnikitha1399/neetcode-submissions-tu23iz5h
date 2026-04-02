class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countt = {}
        counts = {}
        if len(s)!=len(t):
            return False
        for c in range(len(s)):
            counts[s[c]] = 1 + counts.get(s[c],0)
            countt[t[c]] = 1 + countt.get(t[c],0)
        return counts == countt
