/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if(num==0){
        return num;
    } else {
        return (num-1)%9+1;
    }
};