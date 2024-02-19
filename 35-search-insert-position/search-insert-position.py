class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<high):
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid -1
        if high<0:
            high=0
        if nums[high]>=target:
            return high
        else:
            return high+1