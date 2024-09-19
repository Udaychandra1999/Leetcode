class Solution:
    def customSortString(self, order: str, s: str) -> str:
        b=''
        for i in order:
            if i in s:
                b += i*s.count(i)
                s=s.replace(i,'')
        return b+s
        