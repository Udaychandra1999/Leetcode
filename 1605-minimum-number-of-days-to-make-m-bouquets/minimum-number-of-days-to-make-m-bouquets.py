class Solution:
    def is_possible(self,bloomDay,day,m,k)->bool:
        count =0
        boq = 0
        for bloom in bloomDay:
            if bloom<=day:
                count +=1
                if count == k:
                    boq+=1
                    count = 0
            else:
                count = 0
        return boq>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        low,high = min(bloomDay),max(bloomDay)
        while low<high:
            mid = (low+high)//2
            if self.is_possible(bloomDay,mid,m,k):
                high = mid
            else:
                low = mid+1
        return low