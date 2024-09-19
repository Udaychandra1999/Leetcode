class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split(" ")
        fs1 = list(filter(lambda x:x !='' ,s1))
        return len(fs1[-1])