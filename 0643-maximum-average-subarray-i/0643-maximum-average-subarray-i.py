class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum=sum(nums[:k])
        maxSum=currSum
        right=k
        left=0
        for i in range(k,len(nums)):
            currSum=currSum-nums[i-k]+nums[i]
            maxSum=max(maxSum,currSum)
        
        return maxSum/k