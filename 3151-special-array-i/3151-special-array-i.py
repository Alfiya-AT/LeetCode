class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums)==1:
            return True
    
        for i in range(1,len(nums)):
            if (nums[i]%2==0) and (nums[i-1]%2==0):
                return False

            elif (nums[i]%2!=0) and (nums[i-1]%2!=0):
                return False

        return True