class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setA=set()
        for i in nums:
            if i in setA:
                return i
            setA.add(i)
        return setA