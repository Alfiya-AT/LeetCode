class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=0
        left=0
        right=1
        prev=nums[0]
        while right<len(nums):
            if prev<nums[right]:
                mx=max(mx,right-left)
            else:
                left=right
            prev=nums[right]
            right+=1
        return mx+1