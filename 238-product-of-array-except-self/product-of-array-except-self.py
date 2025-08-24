class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        #left to right
        x = 1
        for i in nums:
            res.append(x)
            x = x *i
        x = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= x
            x = x*nums[i]
        return res