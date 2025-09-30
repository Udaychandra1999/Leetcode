class Solution {
public:
    int countDigits(int num) {
        int x = num;
        int res = 0;
        vector<int> c;
        while(x>0){
            c.push_back(x%10);
            x=x/10;
        }
        for(int val:c){
            if(num%val ==0){
                res++;
            }
        }

        return res;
    }
};