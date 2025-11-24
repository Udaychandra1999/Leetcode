class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window,count ={},{}
        res ,resLen= [-1,-1],float("infinity")
        have,need = 0,len(set(t))
        l =0

        for c in t:
            count[c] = 1+count.get(c,0)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)
            
            if c in count and window[c] == count[c]:
                have+=1
            
            while have == need:
                if resLen > (r-l+1):
                    resLen = r-l+1
                    res = [l,r]
                p = s[l]
                window[p]-=1
                if p in count and window[p]<count[p]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
