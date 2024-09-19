class Solution:
   
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        def calctotal(piles:List[int],h:int)->int:
            totalh=0
            for i in piles:
                totalh+=math.ceil(i/h)
            return totalh
        high = piles[0]
        for i in range(1,len(piles)):
            high = max(high,piles[i])
        while low<=high:
            mid = (low+high)//2
            th = calctotal(piles,mid)
            if th<=h:
                high = mid -1
            else:
                low = mid+1
        return low
