class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l=0
        s1_count = {}
        ss_count = {}
        for let in s1:
            s1_count[let] = s1_count.get(let,0) + 1
        
        # for let in s2[l:len(s1)]:
        #         ss_count[let] = ss_count.get(let,0) + 1

        for r in range(len(s2)):
            ss_count[s2[r]] = ss_count.get(s2[r],0) + 1
            while r-l+1>len(s1):
                ss_count[s2[l]]-=1
                if ss_count[s2[l]] == 0:
                    del ss_count[s2[l]]
                l+=1
            if ss_count == s1_count:
                return True
        
        return False
        