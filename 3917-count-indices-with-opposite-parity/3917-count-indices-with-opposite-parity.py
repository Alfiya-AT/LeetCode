
class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[0]*(len(nums))
        even=[0]*(len(nums))
        o=0
        e=0
        for i in range(len(nums)-1,-1,-1):
            odd[i]=o
            even[i]=e
            if nums[i]%2==0:
                e+=1
            else:
                o+=1
            
	    # even=even[::-1]
	    # odd=odd[::-1]
        res=[0]*(len(nums))
        for j in range(len(nums)):
            if nums[j]%2==0:
                res[j]=odd[j]
            else:
                res[j]=even[j]
        return res