class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        l = len(num)-1
        while(l>=0):
            if int(num[l])%2==1:
                return num[0:l+1]
            l-=1
        return ""

