class Solution(object):
    def isHappy(self, n):
        slow=n
        fast=n

        while fast!=1:
            slow=self.sumOfSquare(slow)
            fast=self.sumOfSquare(self.sumOfSquare(fast))
            if fast==1:
                return True
            if slow==fast:
                return False

        return True

    def sumOfSquare(self,n):
        digitSum=0
        while n>0:
            rem=n%10
            digitSum+=(rem**2)
            n//=10
        
        return digitSum
    