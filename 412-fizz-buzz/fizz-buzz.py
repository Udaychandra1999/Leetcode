class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            t=''
            if(i%3==0 and i%5==0):
                t+='FizzBuzz'
            elif(i%3==0):
                t+='Fizz'
            elif(i%5==0):
                t+='Buzz'
            else:
                t+=f'{i}'
            l.append(t)
        return l