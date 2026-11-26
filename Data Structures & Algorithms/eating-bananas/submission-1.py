class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        upper = res
        lower = 1

        while lower<=upper:
            mid = (upper-lower)//2+lower
            if self.canEat(piles, h, mid):
                res = mid
                upper = mid-1
            else:
                lower = mid+1
        
        return res



    
    def canEat(self, piles, h, k):
        time = 0
        for i in piles:
            time+=-(-i//k)
            if time>h:
                return False
        
        return time<=h


        