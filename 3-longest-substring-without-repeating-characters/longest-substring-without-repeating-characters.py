class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d= dict()
        start = 0
        maxLen = 0
        for i,c in enumerate(s):
            if c in d and d[c]>=start:
                start = d[c] +1
            d[c] = i
            maxLen = max(maxLen,i-start+1)
        return maxLen
