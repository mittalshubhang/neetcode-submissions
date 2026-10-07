class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l=0
        s1_count = {}
        for let in s1:
            s1_count[let] = s1_count.get(let,0) + 1

        for r in range(len(s1)-1, len(s2)):
            ss = s2[l:r+1]
            ss_count = {}
            for let in ss:
                ss_count[let] = ss_count.get(let,0) + 1
            
            if ss_count == s1_count:
                return True
            else:
                l+=1
        

        return False
        