class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def letter(digits:str,n:int,res,v):
            if len(digits) == n:
                res.append(''.join(v))
                return
            for i in digit_map[digits[n]]:
                v.append(i)
                letter(digits,n+1,res,v)
                v.pop()
        if len(digits)==0:
            return []
        digit_map= {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}
        if len(digits)==1:
            return digit_map[digits]
        else:
            res=[]
            v=[]
            letter(digits,0,res,v)
        return res

        
                 
        