class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = dict()
        def fn(i,j):
            if (i,j) not in dp:
                if i == (n-1):
                    dp[(i,j)] = triangle[i][j]
                else:
                    dp[(i,j)] = triangle[i][j]+min(fn(i+1,j),fn(i+1,j+1))
            return dp[(i,j)]
        return fn(0,0)