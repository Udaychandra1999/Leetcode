func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)
    for i,ele := range nums {
        if idx,found := mp[target-ele]; found {
            return []int{idx,i}
        }
        mp[ele] = i
    }
    return nil
}