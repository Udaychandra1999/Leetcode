func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
    c:=0
    for i:=0;i<len(hours);i++ {
        if hours[i]>= target {
            c+=1
        }
    }
    return c
}