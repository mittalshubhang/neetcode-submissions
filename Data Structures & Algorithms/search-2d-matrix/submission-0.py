class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper = len(matrix)-1
        lower = 0

        while upper>= lower:
            mid = (upper-lower)//2+lower
            curr_low = matrix[mid][0]
            curr_high = matrix[mid][-1]
            if target> curr_high:
                lower = mid+1
            elif target< curr_low:
                upper = mid-1
            else:
                return self.searchRow(matrix[mid], target)
            
        return False



    def searchRow(self, row: List[int], target: int)-> bool:
        
        upper = len(row)-1
        lower = 0

        while upper>=lower:
            mid = (upper-lower)//2+lower
            curr = row[mid]
            if curr==target:
                return True
            elif target> curr:
                lower = mid+1
            else:
                upper = mid-1
        
        return False
        

        