class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        c =0
        r=[]
        if len(a)>len(b):
            b= ("0"*(len(a)-len(b)))+b
        else:
            a=("0"*(len(b)-len(a))+a)
        a=a[::-1]
        b=b[::-1]
        for x,y in zip(a,b):
            x=int(x)
            y= int(y)
            r.append(x ^ y ^ c)
            c = (x&y)|(y&c)|(c&x)
        if c != 0:
            r.append(c)
        res=""
        for i in r[::-1]:
            res+=str(i)
        return res