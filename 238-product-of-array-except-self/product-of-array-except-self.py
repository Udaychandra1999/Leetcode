class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lar,rar=[],[]
        #left to right
        i=0
        x = 1
        while i< len(nums):
            if i != 0:
                x *= nums[i-1]
            lar.append(x)
            i += 1
        i = len(nums)-1
        x = 1
        while i>=0:
            if i !=len(nums)-1:
                x *= nums[i+1] 
            rar.append(x)
            i -= 1
        res =[]
        for i in range(len(nums)):
            x = lar[i] * rar[len(nums)-i-1]
            res.append(x)
        return res

