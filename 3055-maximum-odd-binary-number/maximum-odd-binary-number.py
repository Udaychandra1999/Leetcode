class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        a=s.count('1')
        return '1' * (s.count('1') - 1) + '0' *(n-a) + '1'
        
