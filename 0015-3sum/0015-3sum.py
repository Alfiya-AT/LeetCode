class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if  nums[i]>0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                self.twoSum(i,nums,res)
        return res

    def twoSum(self,first,nums,res):
        left=first+1
        right=len(nums)-1
        while left<right:
            sumVal=nums[first]+nums[left]+nums[right]
            if sumVal>0:
                right-=1
            elif sumVal<0:
                left+=1
            else:
                res.append([nums[first],nums[left],nums[right]])
                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1] :
                    left+=1
                
                while left<right and nums[right]==nums[right+1] :
                    right-=1

                