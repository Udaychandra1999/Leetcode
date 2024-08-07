class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digit_map= {'2':"abc",
                    '3':"def",
                    '4':"ghi",
                    '5':"jkl",
                    '6':"mno",
                    '7':"pqrs",
                    '8':"tuv",
                    '9':"wxyz"}

        def letter(n:int,v):
            if len(digits) == n:
                res.append(v)
                return
            for i in digit_map[digits[n]]:
                letter(n+1,v+i)

        if len(digits)==0:
            return []
        letter(0,"")
        
        return res

        
                 
        