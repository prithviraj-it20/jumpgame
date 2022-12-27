class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        j=0
        while(i<len(nums)):
            if(j<i):
                return 0
            j=max(nums[i]+i,j)
            i=i+1
        return 1
