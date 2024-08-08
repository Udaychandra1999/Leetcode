class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d ={}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = i
            elif k>=(i-d[nums[i]]):
                return True
            else:
                d[nums[i]] = i
        return False