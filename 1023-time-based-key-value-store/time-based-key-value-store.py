class TimeMap:

    def __init__(self):
        self.mp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((timestamp,value))
        else:
            self.mp[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        li = self.mp[key]
        low,high = 0,len(li)-1
        pos = -1
        while low<=high:
            mid = (low+high)//2
            if li[mid][0]>timestamp:
                high = mid -1
            else:
                pos = mid
                low = mid+1
        if pos == -1:
            return ""
        else:
            return li[pos][1]
            
        
