class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l =[ 0 for i in range(n+1)]
        for x,y in trust:
           l[x-1]-=1
           l[y-1]+=1
        for i in range(n):
            if l[i] == n-1:
                return i+1
        return -1