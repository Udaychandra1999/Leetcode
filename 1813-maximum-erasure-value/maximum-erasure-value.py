class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d=dict()
        score = 0
        start = 0
        curr_sum=0
        for i,val in enumerate(nums):
            if val in d and d[val]>=start:
                while start<= d[val]:
                    curr_sum-=nums[start]
                    start+=1
            d[val] = i
            curr_sum += val
            score = max(score ,curr_sum)
        return score