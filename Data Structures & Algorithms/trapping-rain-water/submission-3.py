class Solution:
    def trap(self, height: List[int]) -> int:
        wt = 0

        l,r = 0, 0
        length = len(height)

        prefix_max = [0]*length
        suffix_max = [0]*length
        

        for i in range(1,length-1):
            prefix_max[i] = max(prefix_max[i-1],height[i-1])
            suffix_max[length-1-i] = max(suffix_max[length-i], height[length-i])

    
        for i in range(length):
            wt += max(min(prefix_max[i], suffix_max[i])-height[i], 0)

        return wt



        