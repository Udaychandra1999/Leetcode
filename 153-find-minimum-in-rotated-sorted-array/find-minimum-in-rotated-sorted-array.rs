impl Solution {
    pub fn min(a:i32,b:i32)->i32 {
        if(a>b){
            b
        }else {
            a
        }
    }
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut res:i32 = nums[0];
        let mut low:i32 = 0;
        let mut high = (nums.len() as i32)-1;
        while low<=high {
            let mid:i32 = (low+high)/2;
            if nums[low as usize]<=nums[mid as usize]{
                res = Solution::min(res,nums[low as usize]);
                low = mid+1;
            }
            else if nums[mid as usize]<= nums[high as usize]{
                res = Solution::min(res,nums[mid as usize]);
                high = mid -1;
            }
        }
        res
    }
}