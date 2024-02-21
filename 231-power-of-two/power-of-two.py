class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        while n and n!=1:
            if n%2:
                return False
            n=n//2
        return True
        