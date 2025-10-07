func isPerfectSquare(num int) bool {
    if num == 1{
        return true
    }
    low:=0
    high:=num
    var mid int
    for low<=high {
        mid= (low+high)/2
        if mid*mid == num {
            return true
        }else if mid*mid > num {
            high = mid -1
        }else {
            low = mid +1
        }
    }
    return false
}