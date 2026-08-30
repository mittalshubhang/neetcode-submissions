class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if num not in hm:
                hm[num] = []
            hm[num].append(i)
        
        for num in nums:
            second = target - num

            if second in hm:
                if second != num:
                    ans = sorted([hm[num][0], hm[second][0]])
                    return ans
                elif len(hm[num]) > 1:
                    return [hm[num][0], hm[num][1]]