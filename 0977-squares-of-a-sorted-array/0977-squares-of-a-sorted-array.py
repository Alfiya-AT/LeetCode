class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        left=0
        right=len(nums)-1
        k=len(nums)-1
        while left<=right:
            if abs(nums[right])>=abs(nums[left]):
                res[k]=nums[right]**2
                right-=1
            else:
                res[k]=nums[left]**2
                left+=1
            k-=1
        return res
        # print(res)