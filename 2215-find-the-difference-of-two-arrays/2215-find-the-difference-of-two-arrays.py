class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        

        nums1=list(set(nums1))
        nums2=list(set(nums2))
        answer=[0,0]
        d1=[]
        d2=[]

        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in d1:
                d1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in d2:
                d2.append(nums2[i])

        answer[0]=d1
        answer[1]=d2

        return answer
