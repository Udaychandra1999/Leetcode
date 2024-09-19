class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nl={}
        for i in range(len(nums)):
            nl[nums[i]]=i
        for i in range(len(nums)):
            c = target - nums[i]
            if c in nl and nl[c]!=i:
                return [nl[c],i]
        return []
