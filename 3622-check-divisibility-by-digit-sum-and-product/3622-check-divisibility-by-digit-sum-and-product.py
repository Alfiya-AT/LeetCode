class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digitSum(n):
            s=0
            while n>0:
                s+=(n%10)
                n//=10
            return s

        def product(n):
            prod=1
            while n>0:
                prod*=(n%10)
                n//=10
            return prod

        return n%(digitSum(n)+product(n))==0