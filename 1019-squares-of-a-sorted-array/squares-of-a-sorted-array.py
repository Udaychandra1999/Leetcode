class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = [i*i for i in nums]
        r.sort()
        return r