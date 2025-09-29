impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        if num ==0 {
            num
        } else {
            (num-1)%9 +1
        }
    }
}