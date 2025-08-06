class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res =[]
        def gen(n):
            if n ==0:
                return [1]
            x = [0] + gen(n-1) + [0]
            li=[]
            for i in range(1,len(x)):
                s = x[i-1]+x[i]
                li.append(s)
            return li
        res = gen(rowIndex)
        return res