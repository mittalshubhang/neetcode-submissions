class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l<r:
            distance = r-l
            area = distance*min(heights[l], heights[r])

            if max_area<area:
                max_area = area
            
            if heights[r]<= heights[l]:
                r-=1
            else:
                l+=1

        return max_area
        

        