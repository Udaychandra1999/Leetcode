class Solution:
    def pivotInteger(self, n: int) -> int:
        x = (n*(n+1)//2)**(0.5)
        cc = int(x)
        return cc if cc == x else -1