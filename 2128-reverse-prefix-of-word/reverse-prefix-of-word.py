class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=-1
        for i in range(len(word)):
            if word[i]==ch:
                idx = i
                break
        s1 = word[:idx+1]
        s1 = s1[::-1]
        s2 = word[idx+1:]
        return s1+s2
        