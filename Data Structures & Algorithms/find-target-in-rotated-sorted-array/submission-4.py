class Solution:
    def search(self, nums: List[int], target: int) -> int:

        numsSub, n = self.findArray(nums, target)
        print(numsSub)

        l,u = 0, len(numsSub)-1

        while l<=u:
            mid = (u+l)//2
            if numsSub[mid]==target:
                return mid+n
            elif numsSub[mid]<target:
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
                    return nums[0:mid], 0
                else:
                    return nums[mid:len(nums)], mid
            else:
                u = mid-1
        return nums,0
        