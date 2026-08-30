class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        for i, letter in enumerate(s):
            if letter in s_map:
                s_map[letter]=s_map[letter]+1
            else:
                s_map[letter] = 1

        for letter in t:
            if letter not in s_map or s_map[letter]==0:
                return False
            s_map[letter]=s_map[letter]-1

        return True
        