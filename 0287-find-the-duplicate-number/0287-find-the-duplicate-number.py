class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # setA=set()
        # for i in nums:
        #     if i in setA:
        #         return i
        #     setA.add(i)
        # return setA


        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        n1=0
        n2=slow

        while n1!=n2:
            n1=nums[n1]
            n2=nums[n2]

        return n1