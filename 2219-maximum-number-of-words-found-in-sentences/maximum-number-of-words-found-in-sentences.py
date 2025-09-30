class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res =0
        for i in sentences:
            x = 0
            for ch in i:
                if ch == " ":
                    x+=1
            res = max(res,x)
        return res+1