class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        al = dict()
        for i in s:
            if i not in al:
                al[i] = 1
            else:
                al[i] = al[i]+1
        for i in range(len(s)):
            if al[s[i]]== 1:
                res = i
                break
        return res
