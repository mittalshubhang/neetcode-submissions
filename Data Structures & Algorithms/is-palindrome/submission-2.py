import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        n = len(s)

        for i in range(int(n/2)):
            if s[i] != s[n-1-i]:
                return False
        
        return True
        