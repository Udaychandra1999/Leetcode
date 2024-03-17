class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,x=[],[]
        newStart,newEnd = newInterval
        x.append(newStart)
        x.append(newEnd)
        for interval in intervals:
            if(newStart>interval[1]):
                l.append(interval)
            elif(newEnd<interval[0]):
                l.append(interval)
            else:
                if(newStart>interval[0]):
                    newStart = interval[0]
                if(newEnd<interval[1]):
                    newEnd = interval[1]
                x[0] = newStart
                x[1] = newEnd
        l.append(x)
        l.sort(key=lambda x: x[0])
        return l
        