class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        right=sum(nums)
        res=[]
        for i in nums:
            right-=i
            res.append(abs(right-left))
            left+=i

        return res