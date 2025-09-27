impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        let mut pos:i32 = 0;
        let mut neg:i32 = 0;
        let mut low:i32 = 0;
        let mut high:i32 = (nums.len() as i32)-1;
        // for positive case
        while low<=high {
            let mut mid:i32 = (low+high)/2;
            if nums[mid as usize]>0 {
                pos += high - mid +1;
                high = mid -1;
            } else {
                low = mid +1;
            }
        }
        // for negative case
        low =0;
        high = (nums.len()as i32)-1;
        while low<=high {
            let mut mid:i32 = (low+high)/2;
            if nums[mid as usize]<0{
                neg += mid - low +1;
                low = mid +1;
            } else {
                high = mid -1;
            }
        }
        if pos>neg {
            pos
        } else {
            neg
        }
    }
}