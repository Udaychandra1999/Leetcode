class Solution:
    def isPossible(self,weights,cap,days)->bool:
        load = 0
        day = 1
        for i in weights:
            if load+i>cap:
                load = i
                day +=1
            else:
                load += i
        return day<=days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights),sum(weights)
        while low<high:
            mid = low + (high-low)//2
            if self.isPossible(weights,mid,days):
                high = mid
            else:
                low = mid+1
        return low