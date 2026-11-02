class Solution:
    def search(self, nums: List[int], target: int) -> int:


        upper = len(nums)-1
        lower = 0

        while upper>=lower:
            mid = lower+((upper-lower)//2)
            print(mid)

            if target == nums[mid]:
                return mid
            elif target< nums[mid]:
                upper = mid-1
            else:
                lower = mid+1
        

        return -1
        