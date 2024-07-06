class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        n = len(candidates)
        def combination(candidates:List[int],n:int,i:int,target:int,s:int,x:List[int],res):
            if(i==n or s>target):
                return
            if(s==target):
                a = list(x)
                res.append(a)
                return
            x.append(candidates[i])
            combination(candidates,n,i,target,s+candidates[i],x,res)
            x.pop()
            combination(candidates,n,i+1,target,s,x,res)
        combination(candidates,n,0,target,0,[],res)
        return res
        