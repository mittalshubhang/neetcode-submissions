class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in s:
            j = t.find(char)
            if j == -1:
                return False
            else:
                t = t[:j]+t[j+1:]

        return True
        