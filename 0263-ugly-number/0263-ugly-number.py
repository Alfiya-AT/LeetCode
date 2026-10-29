class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False


        while n>1:
            divided=False
            for i in (2,3,5):
                if n%i==0:
                    n//=i
                    divided=True
                    break
            if not divided:
                return False

        return True
