class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        n = len(matrix)
        if n>0:
            m = len(matrix[0])
        else:
            return False
        while i<n:
            jl,jh = 0,n-1
            while jl<=jh:
                jm = (jl+jh)//2
                if target <= matrix[jm][m-1] and target>=matrix[jm][0]:
                    i = jm
                    break
                elif target > matrix[jm][m-1]:
                    jl = jm +1
                else:
                    jh = jm -1
            if jl>jh:
                return False
            l,h = 0,m-1
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