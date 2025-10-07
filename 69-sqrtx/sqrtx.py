class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1 :
            return x
        r =x
        rx = 0.5*(r+x/r)
        while(r!=rx):
            r= rx
            rx = 0.5*(r+x/r)
        return int(r)