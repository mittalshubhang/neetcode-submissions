class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = -nums[i]

            l = i+1
            r = len(nums)-1


            while l<r:
                currSum = nums[l]+nums[r]
                if currSum>target:
                    r -=1
                elif currSum<target:
                    l+=1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
        return res
