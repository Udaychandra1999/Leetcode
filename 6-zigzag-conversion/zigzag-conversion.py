class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 or numRows ==1:
            return s
        l=[]
        for i in range(numRows):
            l.append([])
        n  = len(s)
        i=0
        j=0
        flag=True
        while(i<n):
            l[j].append(s[i])
            i+=1
            if j==numRows-1:
                flag = False
            elif j==0:
                flag = True
            if flag:
                j+=1
            else:
                j-=1
        x=[]
        for i in l:
            x.extend(i)
        return "".join(x)