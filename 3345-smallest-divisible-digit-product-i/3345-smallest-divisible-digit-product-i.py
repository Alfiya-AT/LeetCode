class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def product(num):
            prod=1
            while num>0:
                digit=num%10
                num//=10
                prod*=digit
            return prod

        if "0" in str(n):
            return n
        
        while True:
            val=product(n)
            if val%t==0:
                return n
            n+=1

    