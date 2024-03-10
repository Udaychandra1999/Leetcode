class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = list(sorted(nums1))
        n = len(nums1)
        print(n)
        if n%2==0:
            mid = n//2
            print(mid)
            return float(nums1[mid]+nums1[mid-1])/2
        else:
            mid =n//2
            return float(nums1[mid])


        