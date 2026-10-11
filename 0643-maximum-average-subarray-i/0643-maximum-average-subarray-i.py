class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        left=0
        right=0
        currSum=0
        while right<k:
            currSum+=nums[right]
            right+=1

        maxAvg=currSum/k

        while right<len(nums):
            currSum+=nums[right]-nums[left]
            maxAvg=max(maxAvg,currSum/k)
            right+=1
            left+=1

        return maxAvg