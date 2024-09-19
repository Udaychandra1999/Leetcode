class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        i,j=0,1
        m =0
        n = len(s)
        while(i<n and j<=n):
            if len(s[i:j]) == len(set(s[i:j])):
                if len(s[i:j])>=m:
                    m = len(s[i:j])
                j+=1
            else:
                i+=1
        return m

            
        