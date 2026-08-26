class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        count=0
        while i<j:
            sumVal=nums[i]+nums[j]
            if sumVal<target:
                count=count+(j-i)
                i+=1
            else:
                j-=1
        return count