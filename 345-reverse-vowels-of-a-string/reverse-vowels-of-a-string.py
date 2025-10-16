class Solution:
    def reverseVowels(self, s: str) -> str:
        st =[]
        for i in s:
            st.append(i)
        low ,high = 0,len(s)-1
        vowels = "aeiouAEIOU"
        while(low<high):
            while low<high and (st[low] not in vowels):
                low+=1
            while low<high and (st[high]not in vowels):
                high-=1
            if low<high:
                st[low],st[high] = st[high],st[low]
                low+=1
                high-=1
        s = "".join(st)
        return s