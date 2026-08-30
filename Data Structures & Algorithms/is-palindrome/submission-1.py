import math as mt
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        length = len(s)
        if length==0:
            return True
        half_len = mt.floor(length/2)

        for i in range(half_len+1):
            if s[i]!= s[length-i-1]:
                return False

        return True        