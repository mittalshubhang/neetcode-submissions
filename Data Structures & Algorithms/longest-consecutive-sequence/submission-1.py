class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        seen = set(nums)
        init = []
        max_seq = 1

        for i in seen:
            if i-1 not in seen:
                init.append(i)

        for i in init:
            max_set = 1
            j = i+1
            while j in seen:
                max_set+=1
                j+=1
            max_seq = max_set if max_set>max_seq else max_seq


        
        return max_seq