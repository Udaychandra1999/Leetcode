class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else:
            a=1
            b=2
            c=0
            for i in range(n-2):
                c=a+b
                a=b
                b=c
            return b

        