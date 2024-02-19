class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a =0
        for i in digits:
            a = a*10 + i
        a+=1
        return list(map(int,str(a)))