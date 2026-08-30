class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums) 
        left_array = [1]*size
        right_array = [1]*size
        left_mul = 1
        right_mul = 1
        
        res = [1]*size

        for i in range(size):
            left_array[i] = left_mul
            right_array[size-i-1] = right_mul
            left_mul *= nums[i]
            right_mul *= nums[size-i-1]
        
        for i in range(size):
            res[i] = left_array[i]*right_array[i]

        return res

                        