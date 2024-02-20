class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mz = max(nums)
        mi = 0
        res = mz+1
        for i in range(mi,mz+1):
            if i not in nums:
                res = i
        return res
        