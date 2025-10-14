func max(a ,b int)int {
    if a>b {
        return a
    }else {
        return b
    }
}
func lengthOfLongestSubstring(s string) int {
    start := 0
    maxLen := 0
    mp := make(map[rune]int)
    for i,ele := range s {
        idx,ok := mp[ele]
        if ok && idx>=start {
            start = idx+1
        }
        mp[ele] = i
        maxLen = max(maxLen,i-start+1)
    }   
    return maxLen
}