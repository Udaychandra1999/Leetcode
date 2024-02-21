class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res=0
        m=left
        n=right
        while(m!=n):
            m>>=1
            n>>=1
            res+=1
        return m<<res;