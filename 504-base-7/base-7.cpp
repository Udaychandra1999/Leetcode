class Solution {
public:
    string convertToBase7(int num) {
        if(num==0){
            return "0";
        }else if(num<0){
            return "-"+convertToBase7(-num);
        }else if(num<7){
            return to_string(num);
        }else {
            return convertToBase7(num/7)+to_string(num%7);
        }
    }
};