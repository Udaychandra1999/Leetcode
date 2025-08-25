class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        l = set(nums)
        for i in l:
            if i-1 not in l:
                c = 1
                m = i
                while m+1 in l:
                    m += 1
                    c += 1
                res = max(res,c)
        return res

            