class Solution:
    def numberOfSteps(self, num: int) -> int:
        count =0
        if num == 0:
            return 0
        while(num>0):
            if(num%2!=0):
                count+=1
            num=num//2
            count+=1
        return count-1

        