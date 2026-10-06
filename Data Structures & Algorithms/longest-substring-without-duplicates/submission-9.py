class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest_ss = 0
        ss = set()

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            longest_ss = max(longest_ss, r-l+1)
        
        return longest_ss
    