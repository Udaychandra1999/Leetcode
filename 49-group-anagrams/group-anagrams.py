
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count= [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            x = tuple(count)
            if x in res:
                res[x].append(s)
            else:
                res[x] = [s]
        return list(res.values())
        