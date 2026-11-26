class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,u = self.findArray(nums, target)

        

        while l<=u:
            mid = (u+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                u = mid-1
        return -1


    def findArray(self,nums, target):
        l,u = 0, len(nums)-1

        while l<=u:
            mid = (u+l)//2
            if nums[mid]>nums[u]:
                l = mid+1
            elif nums[mid]<nums[max(mid-1,0)]:
                if nums[len(nums)-1]<target:
                    return 0,mid-1
                else:
                    return mid,len(nums)-1
            else:
                u = mid-1
        return 0,len(nums)-1
        