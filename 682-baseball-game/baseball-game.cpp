class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> res;
        for(string s:operations){
            if(s=="D"){
                res.push_back(2*res.back());
            }else if(s=="C"){
                res.pop_back();
            }else if(s=="+"){
                if(res.size()>=2){
                    int x = res[res.size()-1]+res[res.size()-2];
                    res.push_back(x);
                }
            }else {
                res.push_back(stoi(s));
            }
        }
        int total = 0;
        for(int x:res){
            total+=x;
        }
        return total;
    }
};