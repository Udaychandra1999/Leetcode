func mySqrt(x int) int {
    if x==0 || x ==1 {
        return x
    }
    r:=float64(x)
    rx:=0.5*(r+float64(x)/r)
    for r!=rx {
        r = rx
        rx = 0.5*(r+float64(x)/r)
    }
    return int(r)
}