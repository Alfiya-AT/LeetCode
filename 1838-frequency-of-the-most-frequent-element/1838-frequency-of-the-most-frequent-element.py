class Solution(object):
    def maxFrequency(self, nums, k):
        
        # O(N**2)
        # nums.sort()
        # maxFreq = 0

        # for i in range(len(nums)):
        #     currSum = 0

        #     for j in range(i, len(nums)):
        #         currSum += nums[j]

        #         total = nums[j] * (j - i + 1)
        #         operations = total - currSum

        #         if operations > k:
        #             break

        #         maxFreq = max(maxFreq, j - i + 1)

        # return maxFreq




        nums.sort()
        maxfreq=0
        i=0
        j=0
        currSum=0
        while j<len(nums):

            currSum+=nums[j]

            while (nums[j]*(j-i+1)-currSum>k):
                currSum=currSum-nums[i]
                i+=1

            maxfreq=max(maxfreq,j-i+1)
            j+=1

        return maxfreq