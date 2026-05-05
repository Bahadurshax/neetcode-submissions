class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for ch in s:
            if not ch in t or s.count(ch) != t.count(ch):
                return False
        return True
        