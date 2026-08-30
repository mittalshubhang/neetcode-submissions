import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {letter: 0 for letter in string.ascii_lowercase}

        for letter in s:
            seen_s[letter]+=1
        
        for letter in t:
            if seen_s[letter]<=0:
                return False
            else:
                seen_s[letter]-=1
        sum = 0
        for letter in string.ascii_lowercase:
            sum += seen_s[letter]
        
        if sum == 0:
            return True
        else:
            return False


        