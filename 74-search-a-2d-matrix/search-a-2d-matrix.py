class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        n = len(matrix)
        while i<n:
            l,h = 0,len(matrix[i])-1
            while i<n and target>matrix[i][h]:
                i+=1
            if i==n:
                return False
            while l<=h:
                m = (l+h)//2
                if target == matrix[i][m]:
                    return True
                elif target > matrix[i][m]:
                    l = m+1
                else:
                    h = m-1
            return False
        return False