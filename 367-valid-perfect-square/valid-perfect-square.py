class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        low,high = 1,num
        while low<=high:
            mid = (low+high)//2
            if mid*mid == num:
                return True
            elif mid*mid>num:
                high = mid - 1
            else:
                low = mid + 1
        return False