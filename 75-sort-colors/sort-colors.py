class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2=0,0,0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        k=0
        for i in range(c0):
            nums[k]= 0
            k+=1
        for i in range(c1):
            nums[k]=1
            k+=1
        for i in range(c2):
            nums[k]=2
            k+=1

        