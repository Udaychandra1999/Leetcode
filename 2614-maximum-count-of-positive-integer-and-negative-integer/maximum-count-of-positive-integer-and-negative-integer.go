func maximumCount(nums []int) int {
    var low,high,mid,pos,neg int
    low=0
    high = len(nums)-1
    pos =0
    neg = 0
    for low<=high {
        mid = (low+high)/2
        if nums[mid]>0 {
            pos += high-mid+1
            high = mid -1
        } else {
            low = mid +1
        }
    }
    low =0
    high = len(nums)-1
    for low<=high {
        mid = (low+high)/2
        if nums[mid]<0 {
            neg += mid -low +1
            low = mid+1
        } else {
            high = mid -1
        }
    }
    if pos>neg {
        return pos
    } else {
        return neg
    }
}