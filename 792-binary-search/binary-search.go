func search(nums []int, target int) int {
    var l,r int
    l = 0
    r = len(nums)-1
    for l<=r {
        var mid int =(l+r)/2
        if nums[mid] == target {
            return mid
        } else if nums[mid] > target {
            r = mid -1
        } else {
            l = mid +1
        }
    }
    return -1
}