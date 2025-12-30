from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low,high = 1,max(nums)
        while low<high:
            mid = (low+high)//2
            vec = sum(map(lambda x:ceil(x/mid),nums))
            if vec>threshold:
                low = mid+1
            else:
                high = mid
        return low