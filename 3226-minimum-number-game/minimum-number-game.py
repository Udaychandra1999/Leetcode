class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        alice,bob=[],[]
        n = len(nums)
        for i in range(n//2):
            alice.append(nums[2*i])
            bob.append(nums[2*i+1])
        for i in range(len(alice)):
            res.append(bob[i])
            res.append(alice[i])
        return res
