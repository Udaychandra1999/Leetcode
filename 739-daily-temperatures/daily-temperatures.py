class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk =[]
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            e = (temperatures[i],i)
            if len(stk)==0:
                stk.append(e)
                continue
            if i>0 and e[0] > stk[-1][0]:
                while len(stk)>0 and e[0]>stk[-1][0]:
                    x = stk.pop()
                    res[x[1]] = e[1]-x[1]
                stk.append(e)
            else:
                stk.append(e)
        return res 
