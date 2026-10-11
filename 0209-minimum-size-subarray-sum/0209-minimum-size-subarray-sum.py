class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLen=float('inf')

        left=0
        right=0
        currSum=0
        while right<len(nums):
            currSum+=nums[right]
            while currSum>=target:
                minLen=min(minLen,right-left+1)
                currSum-=nums[left]
                left+=1
            right+=1
        
        return 0 if minLen==float('inf') else minLen 
                