class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0 and x<2**31:
            y = int(str(x)[::-1])
            return y if y<(2**31) else 0
        elif x>=(-2**31):
            y = -1* int(str(x*-1)[::-1])
            return y if y>=(-2**31) else 0
        else:
            return 0


        