class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if columnNumber == 0:
            return ""
        n = columnNumber -1
        return self.convertToTitle(n//26)+d[n%26]