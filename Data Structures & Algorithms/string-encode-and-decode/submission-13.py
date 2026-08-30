class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"#"+s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i_of_last_word = -1
        for i in range(len(s)):
            if s[i] == "#" and s[i_of_last_word+1:i].isdigit():
                num = int(s[i_of_last_word+1:i])
                i_of_last_word = i+num
                res.append(s[i+1:i_of_last_word+1])
        
        return res

