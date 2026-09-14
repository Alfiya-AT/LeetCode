class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        if target in nums:
            return 1

        size=float("inf")
        currSum=0

        left=0
        right=0

        while right<len(nums):
            currSum+=nums[right]

            while left<=right and currSum>=target:
                size=min(size,right-left+1)
                currSum-=nums[left]
                left+=1
            
            right+=1

        return size if size!=float("inf") else 0 












        # O(n**2)
        # size=float('inf')
        # currSum=0
        # for i in range(len(nums)):
        #     currSum=0
        #     for j in range(i,len(nums)):
        #         currSum+=nums[j]

        #         if(currSum>=target):
        #             size=min(size,j-i+1)
        #             break


        # return 0 if size==float('inf') else size