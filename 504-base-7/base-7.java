class Solution {
    public String convertToBase7(int num) {
        if(num==0){
            return "0";
        }else if(num<0){
            return "-"+convertToBase7(-num);
        }else if(num<7){
            return Integer.toString(num);
        }else {
            return convertToBase7(num/7)+ (num%7);
        }
    }
}