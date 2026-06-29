class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        res=[]
        val=[x for x in range(nums[0],nums[-1]+1) ]
        for i in val:
            if i not in nums:
                res.append(i)

        return res