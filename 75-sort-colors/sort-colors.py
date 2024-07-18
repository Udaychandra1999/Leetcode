class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = dict()
        for i in nums:
            if i not in c:
                c[i] =1
            else:
                c[i] = c[i] +1
        k=0
        for i in sorted(c.keys()):
            while c[i]>0:
                nums[k] = i
                k+=1
                c[i]-=1

        