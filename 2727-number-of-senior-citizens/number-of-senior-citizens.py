class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            x=int(i[11:13])
            if(x>60):
                count+=1
        return count