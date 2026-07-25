class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n<=9:
        #     return n
        # elif len(str(n))==2:
        #     num=str(n)
        #     return int(num[-1])*int(num[-2])
        # res=[int(x) for x in str(n)]
        # res.sort()
        # return res[-1]*res[-2]

        m=sorted(str(n))
        return int(m[-1])*int(m[-2])