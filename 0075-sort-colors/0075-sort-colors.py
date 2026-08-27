class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        k=0

        while k<=j:
            if nums[k]==1:
                k+=1
            elif nums[k]==2:
                temp=nums[j]
                nums[j]=nums[k]
                nums[k]=temp
                j-=1
            else:
                temp=nums[i]
                nums[i]=nums[k]
                nums[k]=temp
                i+=1
                k+=1

        return nums