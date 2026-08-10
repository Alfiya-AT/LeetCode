class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def squareSum(num):
            res=0
            while num>0:
                rem=num%10
                res+=(rem**2)
                num=num//10

            return res
        def digitSum(num):
            res=0
            while num>0:
                rem=num%10
                res+=rem
                num//=10
            return res
        dSum=digitSum(n)
        sSum=squareSum(n)
        return (sSum-dSum)>=50