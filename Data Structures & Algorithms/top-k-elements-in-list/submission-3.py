class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        counter = [0] *(len(nums)+1)
        sol=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            
        for key, value in freq.items():
            if counter[value] == 0:
                counter[value] = [key]
            else:
                counter[value].append(key)
        for i in reversed(counter):
            if i !=0:
                sol.extend(i)
                if len(sol)==k:
                    return sol

        