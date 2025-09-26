func Min(a,b int) int {
    if a>b {
        return b
    } else {
        return a
    }
}
func findMin(nums []int) int {
    var res int = nums[0]
    var low,high,mid int
    low = 0
    high = len(nums)-1
    for low<=high {
        mid = (low+high)/2
        if nums[low]<= nums[mid] {
            res = Min(res,nums[low])
            low = mid +1
        } else if nums[mid]<= nums[high]{
            res = Min(res,nums[mid])
            high = mid -1
        }
    }
    return res
}
