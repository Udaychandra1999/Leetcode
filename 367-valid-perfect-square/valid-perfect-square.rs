impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num == 1 {
            return true
        }
        let mut low:i64 = 1;
        let mut high:i64 = num.into();
        while low<=high {
            let mid:i64 = (low+high)/2;
            if mid*mid  == num as i64{
                return true
            }else if mid*mid > num as i64 {
                high = mid -1;
            } else {
                low = mid + 1;
            }
        }
        false
    }
}