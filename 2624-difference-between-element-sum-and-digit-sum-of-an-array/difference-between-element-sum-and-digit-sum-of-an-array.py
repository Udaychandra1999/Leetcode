class Solution:
    def abs(a:int):
        if a>0:
            return a
        else:
            return -a
    def differenceOfSum(self, nums: List[int]) -> int:
        s,ds=0,0
        for i in nums:
            s+=i
            x=i
            while x>0:
                ds+=x%10
                x=x//10
        return abs(s-ds)
            