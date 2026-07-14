class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        res=0
        for key,val in d.items():
            if val%k==0:
                res+=(val*key)

        if res%k==0:
            return res


        return 0