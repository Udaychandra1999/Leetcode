class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[]
        def gen(n,res):
            if n ==1:
                res.append([1])
                return [1]
            x = [0] + gen(n-1,res) + [0]
            li=[]
            for i in range(1,len(x)):
                s = x[i-1]+x[i]
                li.append(s)
            res.append(li)
            return li
        row = gen(numRows,res)
        return res