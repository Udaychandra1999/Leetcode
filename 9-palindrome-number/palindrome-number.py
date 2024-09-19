class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n =x
        res=0
        while(n>0):
            res = res*10+n%10
            n=n//10
        return res==x
        
        