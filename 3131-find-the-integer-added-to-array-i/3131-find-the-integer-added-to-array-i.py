class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # if nums1==nums2:
        #     return 0
        # nums1.sort()
        # nums2.sort()
        # diff=nums2[0]-nums1[0]
        # for i in range(1,len(nums1)):
        #     if (nums2[i]-nums1[i])!=diff:
        #         return 
        # return diff


        return min(nums2)-min(nums1)