class Solution:
    def findMin(self, nums: List[int]) -> int:
        upper = len(nums)-1
        lower = 0 

        while lower<=upper:
            mid = (upper-lower)//2+lower
            if nums[mid]>nums[upper]:
                lower = mid+1
            elif nums[mid]<= nums[max(mid-1,0)]:
                return nums[mid]
            else:
                upper = mid-1
        