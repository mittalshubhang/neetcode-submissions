class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        s_count = {}
        ss = ""
        have = 0
        for let in t:
            t_count[let]=t_count.get(let, 0)+1
            s_count[let]=0
        need = len(t_count)
        l = 0

        for r in range(len(s)):
            valid_ss = ""
            if s[r] in s_count:
                s_count[s[r]] = s_count.get(s[r],0)+1
                if s_count[s[r]] == t_count[s[r]]:
                    have+=1

            while have==need:
                valid_ss = s[l:r+1]
                if s_count.get(s[l],0)!=0:
                    s_count[s[l]]-=1
                    if s_count[s[l]]<t_count[s[l]]:
                        have-=1
                l+=1

                if len(ss)>len(valid_ss) or len(ss)==0:
                    ss=valid_ss
        
        return ss
        
