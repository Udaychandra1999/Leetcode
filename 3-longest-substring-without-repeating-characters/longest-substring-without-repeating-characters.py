class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = dict()
        l =0
        longest = 0
        for r in range(len(s)):
            if s[r] in ch:
                l = max(l,ch[s[r]]+1)
            ch[s[r]] = r
            longest = max(longest,(r-l+1))
        return longest  
                
                