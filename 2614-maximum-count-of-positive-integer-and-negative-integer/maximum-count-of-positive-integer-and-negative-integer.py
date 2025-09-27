class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos,neg =0,0
        low,high = 0,len(nums)-1
        #positive phase
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>0:
                pos +=high-mid+1
                high = mid -1
            else:
                low = mid +1
        #negative phase
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<0:
                neg += mid-low+1
                low = mid+1
            else:
                high = mid -1
        return max(pos,neg)

        