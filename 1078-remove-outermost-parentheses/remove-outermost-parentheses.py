class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        res=''
        for i in s:
            if i=='(':
                if cnt!=0:
                    res+=i
                cnt+=1
            elif i==')':
                if cnt!=1:
                    res+=i
                cnt-=1
        print(cnt)
        return res