func findWordsContaining(words []string, x byte) []int {
    res:=[]int{}
    for i,ele := range words {
        for j:=0;j<len(ele);j++{
            if x == ele[j] {
                res = append(res,i)
                break
            }
        }
    }
    return res
}