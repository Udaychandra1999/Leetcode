class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp ;
        mp[0]=1;
        int s=0,count=0;
        for(int i:nums)
        {
            s+=i;
            if(mp.find(s-k)!=mp.end())
            {
                count+=mp[s-k];
            }
            if(mp.find(s)!=mp.end())
            {
                mp[s]+=1;
            }
            else
            {
                mp[s] =1;
            }
        }
        return count;
    }
};