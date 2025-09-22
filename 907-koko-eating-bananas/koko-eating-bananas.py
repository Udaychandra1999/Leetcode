class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(a:float)->int:
            x= int(a)
            if a == x:
                return a
            else:
                return x+1 
        res = max(piles)
        low,high = 1,max(piles)
        while(low<=high):
            mid = (low+high)//2
            vec = list(map(lambda i:ceil(i/mid),piles))
            if sum(vec)<=h:
                res = min(res,mid)
                high = mid-1
            else:
                low = mid+1
        return res

