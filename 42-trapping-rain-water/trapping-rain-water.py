class Solution:
    def trap(self, height: List[int]) -> int:
        lwall,rwall =0,0
        n = len(height)
        lmax,rmax=[0]*n,[0]*n
        for i in range(n):
            lmax[i] = lwall
            lwall = max(lwall,height[i])
            j = -i-1
            rmax[j] = rwall
            rwall = max(rwall,height[j])
        res =0
        for i in range(n):
            pot = min(lmax[i],rmax[i])
            res += max(0,pot-height[i])
        return res
